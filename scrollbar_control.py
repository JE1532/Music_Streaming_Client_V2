import time
import datetime
from threading import Event


TIME_STEP = 0.1

TERMINATE = 'exit!'


class InfoEvent(Event):
    """
    Event that bears information (used exclusively in streaming mechanism)
    """
    def __init__(self):
        """
        Initialize an infoEvent.
        """
        super().__init__()
        self.info = None
        self.is_pause_play = False  # does current event activation indicate that audio plaing has been pause or resumed? (bool)


    def set(self, info):
        """
        set event and add info.
        :param info: information for event.
        :return: None
        """
        self.info = info
        self.is_pause_play = False
        super().set()


    def pause_or_play(self):
        """
        Set event while indicating that the event indicated is a pause or resume of audio playing.
        :return:
        """
        self.is_pause_play = True
        super().set()



def scrollbar_control(event, gui, scrollbar_lock, paused_event):
    """
    Executes scrollbar control thread.
    :param event: (InfoEvent) for when the player moves the scrollbar.
    :param gui: (Ui_MainQWindow) for accessing gui aspects of scrollbar.
    :param scrollbar_lock: (threading.Lock)
    :param paused_event: (threading.Event) triggered when playing is paused.
    :return:
    """
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
                    if event.info == TERMINATE:
                        return
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
            gui.set_scrollbar_value(current_time.total_seconds() / track_length, current_time.total_seconds(), track_length)
        time.sleep(TIME_STEP)
