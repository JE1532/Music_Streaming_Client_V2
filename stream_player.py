import math
import pyaudio
import wave
import io
import datetime


FORMAT = pyaudio.paInt16
RATE = 44100
CHUNK_SIZE = 256

NEXT_SONG = 'next_song'
TERMINATE = 'exit!'


def player(play_queue, pause_event, play_event, change_track_event, play_next_song_signal, file_system_clear_approved):
    """
    Runs Stream_Player thread. Blocks.
    :param play_queue: (Queue) of (file_path, num_channels) of audio to play (num_channels = number of audio channels in file, is None unless changed since last file)
    :param pause_event: (threading.Event) triggered when playing is paused.
    :param play_event: (threading.Event) triggered when playing is resumed.
    :param change_track_event: (threading.Event) triggered when changing song.
    :param play_next_song_signal: (Pyside6.QtCore.Signal) emitted when current song is done playing.
    :param file_system_clear_approved: (threading.Event) triggered when player is not using file system.
    :return:
    """
    p = pyaudio.PyAudio()
    num_channels = None
    output = None
    while True:
        file_system_clear_approved.set()
        input_path, num_channels = play_queue.get()
        if input_path == TERMINATE:
            return
        if num_channels != None:
            output = p.open(format=8,
                            channels=num_channels,
                            rate=RATE,
                            output=True,
                            )
        change_track_event.wait()
        change_track_event.clear()
        if input_path == NEXT_SONG:
            play_next_song_signal.emit()
            continue
        with wave.open(input_path, 'rb') as input:
            play(input, output, pause_event, play_event, change_track_event)
            #print('another file')


def play(input, output, pause_event, play_event, change_track_event):
    #print('start:', datetime.datetime.now())
    while len(data := input.readframes(CHUNK_SIZE)):
        output.write(data)
        if pause_event.isSet():
            pause_event.clear()
            play_event.wait()
            play_event.clear()
        if change_track_event.isSet():
            return
    change_track_event.set()
    #print('end: ', datetime.datetime.now())
