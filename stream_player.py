import math
import pyaudio
import wave
import io
import datetime


FORMAT = pyaudio.paInt16
RATE = 44100
CHUNK_SIZE = 1024


def player(play_queue, playing_event, change_track_event):
    p = pyaudio.PyAudio()
    output = p.open(format=8,
                    channels=2,
                    rate=RATE,
                    output=True,
                    )
    while True:
        with wave.open(play_queue.get(), 'rb') as input:
            play(input, output, playing_event, change_track_event)
            #print('another file')


def play(input, output, playing_event, change_track_event):
    #print('start:', datetime.datetime.now())
    while len(data := input.readframes(CHUNK_SIZE)):
        output.write(data)
        if playing_event.isSet():
            playing_event.clear()
            playing_event.wait()
            playing_event.clear()
        if change_track_event.isSet():
            change_track_event.clear()
            break
    #print('end: ', datetime.datetime.now())
