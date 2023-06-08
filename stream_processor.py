from pydub import AudioSegment
from queue import Queue
from os.path import dirname
import os
import subprocess


M3U8 = b'#EXTM3U'
EXTINF = b'EXTINF'

REQ = lambda dir, relative_path: f"""GET /{dir + '/' + relative_path} HTTP/1.1@"""
SEGMENT = lambda serial: f'segment{serial}.wav'
TEMP_START_SEG = 'temp_start_file.wav'
#CONVERTION_COMMAND = ['ffmpeg', '-y', '-f', 'mp4', '-read_ahead_limit', '-1', '-i', 'cache:pipe:0', '-acodec', 'pcm_s16le', '-vn', '-f', 'wav', '-']
CONVERTION_COMMAND = ['ffmpeg', '-i', 'input.m4a', '-f', 'wav', '-']
#p = subprocess.Popen(conversion_command, stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
IGNORE = None
NEXT_SONG = 'next_song'


def stream_processor(input_queue, play_queue, send_queue, expect_m3u8_and_url, playing_event, scrollbar_lock, fetch_change_event, player_change_track_event):
    playlist = Queue()
    time_into_first_segment = 0
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
            with scrollbar_lock:
                playing_event.set((track_length, 0))  # (track_length, current_time)
        elif expect_m3u8_and_url[0]:
            continue
        elif fetch_change_event.isSet():
            track_length, new_time, is_new_song = fetch_change_event.info
            time_into_first_segment = change_time(playlist, play_queue, segment_times, segment_reqs, new_time)
            fetch_change_event.clear()
            player_change_track_event.set()
            next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event)
            if next_request:
                send_queue.put(next_request.encode())
                print(next_request)
        else:
            segment = process_m4a(body, segment_num)
            downloaded_segments[segment_num] = segment
            play_queue.put(handle_segment(segment, is_first_seg, time_into_first_segment))
            next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event)
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
                    next_request, segment_num, is_first_seg = play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event)
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


def process_m4a(data, segment_num):
    with open('input.m4a', 'wb') as input_file_for_ffmpeg:
        input_file_for_ffmpeg.write(data)
    with open(os.devnull, 'rb') as devnull:
       p = subprocess.Popen(CONVERTION_COMMAND, stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_out, p_err = p.communicate()
    assert p.returncode == 0
    segment = bytes(p_out)
    with open(SEGMENT(segment_num), 'wb') as f:
        f.write(segment)
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


def handle_segment(segment, is_first_seg, time_into_first_segment):
    if is_first_seg:
        audioseg = AudioSegment.from_file(segment, 'wav')
        audioseg[time_into_first_segment * 1000:].export(TEMP_START_SEG, format='wav')
        segment = TEMP_START_SEG
    return segment


def play_downloaded_segments(playlist, downloaded_segments, play_queue, time_into_first_segment, fetch_change_event):
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
        play_queue.put(handle_segment(segment, is_first_seg, time_into_first_segment))
    if not loop_broken:
        return None, None, None
    return next_request, segment_num, is_first_seg
