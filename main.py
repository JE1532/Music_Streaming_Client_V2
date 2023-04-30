import threading
from queue import Queue
import socket
import multiprocessing
from receiver import Receiver
from general_processor import GeneralProcessor
from send_handler import sender
from user_processor import UserProcessor
from stream_processor import stream_processor
from stream_player import player
from scrollbar_control import scrollbar_control, InfoEvent
from gui import Ui_MainWindow as MainWindow



SERVER = ('127.0.0.1', 9010)


def play_stream(stream_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, gui, player_playing_event, player_fetching_event, scrollbar_paused_event):
    play_queue = Queue()
    player_change_track_event = threading.Event()
    stream_processor_thread = threading.Thread(target=stream_processor, args=(stream_queue, play_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, player_fetching_event, player_change_track_event))
    threads = []
    threads.append(stream_processor_thread)
    stream_player_thread = threading.Thread(target=player, args=(play_queue, player_playing_event, player_change_track_event))
    threads.append(stream_player_thread)
    scrollbar_control_thread = threading.Thread(target=scrollbar_control, args=(scrollbar_playing_event, gui, scrollbar_lock, scrollbar_paused_event))
    threads.append(scrollbar_control_thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(SERVER)
    print('connected!')
    threads = []
    rec_queue = Queue()
    receiver = Receiver(lambda: sock.recv(100000), rec_queue)
    receiver_thread = threading.Thread(target=receiver.start)
    threads.append(receiver_thread)
    stream_queue = multiprocessing.Queue()
    user_replies_queue = Queue()
    gui_msg_queue = Queue()
    general_processor = GeneralProcessor(rec_queue, stream_queue, user_replies_queue, gui_msg_queue)
    general_processor_thread = threading.Thread(target=general_processor.start)
    threads.append(general_processor_thread)
    send_queue = Queue()
    sender_thread = threading.Thread(target=sender, args=(send_queue, sock))
    threads.append(sender_thread)
    login_finished_event = threading.Event()
    login_approved = [False]
    user_processor = UserProcessor(login_finished_event, login_approved, user_replies_queue)
    user_processor_thread = threading.Thread(target=user_processor.start)
    threads.append(user_processor_thread)
    expect_m3u8_and_url = [False, '']
    scrollbar_playing_event = InfoEvent()
    player_playing_event = threading.Event()
    player_fetching_event = InfoEvent()
    scrollbar_lock = threading.Lock()
    scrollbar_paused_event = threading.Event()
    gui = MainWindow()
    gui_thread = threading.Thread(target=gui.start, args=(send_queue, login_finished_event, login_approved, expect_m3u8_and_url, scrollbar_playing_event, player_playing_event, player_fetching_event, scrollbar_paused_event, gui_msg_queue))
    gui_thread.start()
    stream = threading.Thread(target=play_stream, args=(stream_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, gui, player_playing_event, player_fetching_event, scrollbar_paused_event))
    stream.start()


    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
