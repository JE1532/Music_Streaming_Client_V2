import math
import pyaudio
import wave
import io
import datetime


FORMAT = pyaudio.paInt16
RATE = 44100
CHUNK_SIZE = 256

NEXT_SONG = 'next_song'


def player(play_queue, pause_event, play_event, change_track_event, play_next_song_signal, file_system_clear_approved):
    p = pyaudio.PyAudio()
    output = p.open(format=8,
                    channels=1,
                    rate=RATE,
                    output=True,
                    )
    while True:
        file_system_clear_approved.set()
        input_path = play_queue.get()
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
