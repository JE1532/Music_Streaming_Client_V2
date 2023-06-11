from pydub import AudioSegment
from queue import Queue
from os.path import dirname
import os
import subprocess
import threading


M3U8 = b'#EXTM3U'
EXTINF = b'EXTINF'

REQ = lambda dir, relative_path: f"""GET /{dir + '/' + relative_path} HTTP/1.1@"""
SEGMENT = lambda serial: f'segment{serial}.wav'
TEMP_START_SEG = 'temp_start_file.wav'
#CONVERTION_COMMAND = ['ffmpeg', '-y', '-f', 'mp4', '-read_ahead_limit', '-1', '-i', 'cache:pipe:0', '-acodec', 'pcm_s16le', '-vn', '-f', 'wav', '-']
CONVERTION_COMMAND = ['ffmpeg', '-f', 'mpegts', '-i', 'input.ts', '-f', 'wav', '-sample_fmt', 's16', '-ar', '44100', '-']
FFPROBE_COMMAND_TO_GET_CHANNELS = ['ffprobe', '-i', 'pipe:0', '-show_entries', 'stream=channels', '-v', 'quiet']
GET_NUM_CHANNELS = lambda p_out: int(dict([line.split('=') if '=' in line else (line, line) for line in p_out.decode().split('\n')])['channels'])
#p = subprocess.Popen(conversion_command, stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
IGNORE = None
NEXT_SONG = 'next_song', None


class FileSystemWrapper:
    def __init__(self, path_maker, segment_name):
        self.path_maker = path_maker
        self.segment_name = segment_name
        self.segname_to_filename = dict()
        self.available_filenames = set()
        self.next_filenum = 0
        self.lock = threading.Lock()


    def save(self, segname, data):
        self.lock.acquire()
        if len(self.available_filenames) == 0:
            filename = self.path_maker(self.next_filenum)
            self.next_filenum += 1
        else:
            filename = self.available_filenames.pop()
        self.segname_to_filename[segname] = filename
        self.lock.release()
        with open(filename, 'wb') as f:
            f.write(data)


    def clear(self, wait_for=None):
        self.lock.acquire()
        filenames_for_clearing = set(self.segname_to_filename.values())
        self.segname_to_filename = dict()
        self.lock.release()
        releaser = threading.Thread(target=self.free_filenames, args=(filenames_for_clearing, wait_for))
        releaser.start()


    def free_filenames(self, filenames, wait_for):
        if wait_for:
            wait_for.wait()
            wait_for.clear()
        for filename in filenames:
            self.free_filename(filename)


    def free_filename(self, filename):
        os.remove(filename)
        self.lock.acquire()
        self.available_filenames.add(filename)
        self.lock.release()


    def get_path(self, segname):
        return self.segname_to_filename[segname]


def stream_processor(input_queue, play_queue, send_queue, expect_m3u8_and_url, playing_event, scrollbar_lock, fetch_change_event, player_change_track_event, file_system_clear_approved):
    playlist = Queue()
    time_into_first_segment = 0
    file_system_wrapper = FileSystemWrapper(SEGMENT, SEGMENT)
    clear_file_system = False
    while True:
        current_msg_encoded = input_queue.get()
        if not current_msg_encoded == IGNORE:
            separation_index = bytes.find(current_msg_encoded, b'\r\n\r\n')
            assert separation_index != -1
            headers = current_msg_encoded[:separation_index].decode()
            body = current_msg_encoded[separation_index + 4:]
            lines = headers.split('\n')
        try:
            status_code = lines[0].split(' ')[1]
            if not status_code == '200':
                raise Exception('HTTP Status Code not 200')
        except:
            raise Exception('HLS Stream response not valid HTTP')
        if body[:len(M3U8)] == M3U8 and expect_m3u8_and_url[0]:
            del playlist
            playlist = Queue()
            dir = dirname(expect_m3u8_and_url[1])
            track_length, segment_times, segment_reqs = process_m3u8(body, dir, playlist)
            fetch_change_event.info = (track_length, 0, False)
            next_request, segment_num, is_first_seg = playlist.get()
            #send_queue.put(next_request)
            #print(next_request)
            input_queue.put(IGNORE)
            expect_m3u8_and_url[0] = False
            downloaded_segments = dict()
            clear_file_system = True
            with scrollbar_lock:
                playing_event.set((track_length, 0))  # (track_length, current_time)
        elif expect_m3u8_and_url[0]:
            continue
        elif fetch_change_event.isSet():
            track_length, new_time, is_new_song = fetch_change_event.info
            time_into_first_segment = change_time(playlist, play_queue, segment_times, segment_reqs, new_time)
            fetch_change_event.clear()
            player_change_track_event.set()
            if clear_file_system:
                file_system_clear_approved.clear()
                file_system_wrapper.clear(wait_for=file_system_clear_approved)
                clear_file_system = False
            next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event, file_system_wrapper)
            if next_request:
                send_queue.put(next_request.encode())
                print(next_request)
        else:
            segment = process_m4a(body, segment_num, file_system_wrapper)
            downloaded_segments[segment_num] = segment
            play_queue.put(handle_segment(segment, is_first_seg, time_into_first_segment, file_system_wrapper))
            next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event, file_system_wrapper)
            if next_request:
                send_queue.put(next_request.encode())
                print(next_request)
            else:
                print('done downloading')
                while True:
                    play_queue.put(NEXT_SONG)
                    fetch_change_event.wait()
                    track_length, curr_time, is_new_song = fetch_change_event.info
                    if is_new_song:
                        break
                    time_into_first_segment = change_time(playlist, play_queue, segment_times, segment_reqs, curr_time)
                    player_change_track_event.set()
                    fetch_change_event.clear()
                    next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event, file_system_wrapper)
                    if next_request:
                        fetch_change_event.clear()
                        send_queue.put(next_request.encode())
                        print(next_request)
                        break
                    fetch_change_event.clear()
    print("terminating?")


def process_m3u8(data, dir, playlist):
    labels = data.split(b'#')
    track_length = 0
    segment_num = 0
    segment_times = []
    segment_reqs = []
    for label in labels:
        components = label.split(b'\n')[:-1]
        if len(components) == 2 and components[0][:len(EXTINF)] == EXTINF:
            try:
                segment_length = float(components[0].split(b':')[1][:-1])
                segment_req = REQ(dir, components[1].decode())
                playlist.put((segment_req, segment_num, False))
            except:
                raise Exception('Invalid m3u8 file received')
            track_length += segment_length
            segment_times.append(track_length)
            segment_reqs.append(segment_req)
            segment_num += 1
    return track_length, segment_times, segment_reqs


def process_m4a(data, segment_num, file_system_wrapper):
    with open('input.ts', 'wb') as input_file_for_ffmpeg:
        input_file_for_ffmpeg.write(data)
    with open(os.devnull, 'rb') as devnull:
       p = subprocess.Popen(CONVERTION_COMMAND, stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_out, p_err = p.communicate()
    assert p.returncode == 0
    segment = bytes(p_out)
    file_system_wrapper.save(SEGMENT(segment_num), segment)
    return SEGMENT(segment_num)


def change_time(playlist, play_queue, segment_times, segment_reqs, new_time):
    while not playlist.empty():
        playlist.get()
    while not play_queue.empty():
        play_queue.get()
    i = 0
    while i < len(segment_times) and new_time > segment_times[i]:
        i += 1
    if i == len(segment_times):
        return
    seg_start = segment_times[i - 1] if i > 0 else 0
    time_into_first_segment = new_time - seg_start
    playlist.put((segment_reqs[i], i, True))
    for segment_num in range(i + 1, len(segment_reqs)):
        playlist.put((segment_reqs[segment_num], segment_num, False))
    return time_into_first_segment


def handle_segment(segment, is_first_seg, time_into_first_segment, file_system_wrapper):
    num_channels = None
    if is_first_seg:
        audioseg = AudioSegment.from_file(file_system_wrapper.get_path(segment), 'wav')
        audioseg[time_into_first_segment * 1000:].export(TEMP_START_SEG, format='wav')
        with open(TEMP_START_SEG, 'rb') as f:
            data = f.read()
            file_system_wrapper.save(TEMP_START_SEG, data)
        p = subprocess.Popen(FFPROBE_COMMAND_TO_GET_CHANNELS, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p_out, p_err = p.communicate(input=data)
        assert p.returncode == 0
        num_channels = GET_NUM_CHANNELS(p_out)
        segment = TEMP_START_SEG
    return file_system_wrapper.get_path(segment), num_channels


def play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event, file_system_wrapper):
    next_request, segment_num, is_first_seg = None, None, None
    loop_broken = False
    while not playlist.empty():
        if fetch_change_event.isSet():
            loop_broken = True
            break
        next_request, segment_num, is_first_seg = playlist.get()
        if not segment_num in downloaded_segments:
            loop_broken = True
            break
        segment = downloaded_segments[segment_num]
        play_queue.put(handle_segment(segment, is_first_seg, time_into_first_segment, file_system_wrapper))
    if not loop_broken:
        return None, None, None
    return next_request, segment_num, is_first_seg
