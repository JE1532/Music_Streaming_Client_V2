import time
import datetime
from threading import Event


TIME_STEP = 0.1


class InfoEvent(Event):
    def __init__(self):
        super().__init__()
        self.info = None
        self.is_pause_play = False


    def set(self, info):
        self.info = info
        self.is_pause_play = False
        super().set()


    def pause_or_play(self):
        self.is_pause_play = True
        super().set()



def scrollbar_control(event, gui, scrollbar_lock, paused_event):
    currently_playing = False
    track_length, current_time = 0, datetime.timedelta(seconds=0)
    start = datetime.datetime.now()
    while True:
        if track_length <= current_time.total_seconds():
            currently_playing = False
            #print(datetime.datetime.now() - start)
        if not currently_playing:
            event.wait()
        with scrollbar_lock:
            if event.isSet():
                if not event.is_pause_play or currently_playing == False:
                    currently_playing = True
                    track_length, current_time_in_secs = event.info
                    #print(track_length)
                    start = datetime.datetime.now() - datetime.timedelta(seconds=current_time_in_secs)
                    #print('scrollb starts:', start)
                    paused_event.clear()
                else:
                    currently_playing = False
                    event.info = (track_length, current_time.total_seconds())
                    paused_event.set()
                event.clear()
            current_time = datetime.datetime.now() - start
            gui.set_scrollbar_value(current_time.total_seconds() / track_length)
        time.sleep(TIME_STEP)
