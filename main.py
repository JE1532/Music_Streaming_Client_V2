import threading
import sys
import ssl
from queue import Queue
import socket
import multiprocessing
from PySide6 import QtCore as qtc

from receiver import Receiver
from general_processor import GeneralProcessor
from send_handler import sender
from user_processor import UserProcessor
from stream_processor import stream_processor
from stream_player import player
from scrollbar_control import scrollbar_control, InfoEvent
from gui import Ui_MainWindow as MainWindow
from socket_wrapper import SocketWrapper



SERVER = ('127.0.0.1', 9010)
ROOTCA = 'rootCA.crt'

TERMINATE = 'exit!'


class StreamReceiver(qtc.QObject):
    play_next_song_signal = qtc.Signal()

    def __init__(self, gui):
        super().__init__()
        self.gui = gui


def play_stream(stream_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, gui, player_pause_event, player_play_event, player_fetching_event, scrollbar_paused_event, play_next_song_signal):
    play_queue = Queue()
    player_change_track_event = threading.Event()
    file_system_clear_approved = threading.Event()
    stream_processor_thread = threading.Thread(target=stream_processor, args=(stream_queue, play_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, player_fetching_event, player_change_track_event, file_system_clear_approved))
    threads = []
    threads.append(stream_processor_thread)
    stream_player_thread = threading.Thread(target=player, args=(play_queue, player_pause_event, player_play_event, player_change_track_event, play_next_song_signal, file_system_clear_approved))
    threads.append(stream_player_thread)
    scrollbar_control_thread = threading.Thread(target=scrollbar_control, args=(scrollbar_playing_event, gui, scrollbar_lock, scrollbar_paused_event))
    threads.append(scrollbar_control_thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = ssl.wrap_socket(
        sock,
        ssl_version=ssl.PROTOCOL_TLSv1_2,
        do_handshake_on_connect=True,
        cert_reqs=ssl.CERT_REQUIRED,
        ca_certs=ROOTCA
    )
    sock.connect(SERVER)
    sock_save = sock
    sock = SocketWrapper(sock)
    print('connected!')
    threads = []
    rec_queue = Queue()
    receiver = Receiver(lambda: sock.recv(), rec_queue)
    receiver_thread = threading.Thread(target=receiver.start)
    threads.append(receiver_thread)
    stream_queue = multiprocessing.Queue()
    user_replies_queue = Queue()
    gui_msg_queue = Queue()
    upload_resp_queue = Queue()
    general_processor = GeneralProcessor(rec_queue, stream_queue, user_replies_queue, gui_msg_queue, upload_resp_queue)
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
    player_pause_event = threading.Event()
    player_play_event = threading.Event()
    player_fetching_event = InfoEvent()
    scrollbar_lock = threading.Lock()
    scrollbar_paused_event = threading.Event()
    gui = MainWindow()
    stream_rec = StreamReceiver(gui)
    stream_rec.play_next_song_signal.connect(gui.play_next_song)
    stream = threading.Thread(target=play_stream, args=(stream_queue, send_queue, expect_m3u8_and_url, scrollbar_playing_event, scrollbar_lock, gui, player_pause_event, player_play_event, player_fetching_event, scrollbar_paused_event, stream_rec.play_next_song_signal))
    threads.append(stream)


    for thread in threads:
        thread.start()

    gui.start(send_queue, login_finished_event, login_approved, expect_m3u8_and_url, scrollbar_playing_event, player_pause_event, player_play_event, player_fetching_event, scrollbar_paused_event, gui_msg_queue, upload_resp_queue)

    for q in (send_queue, rec_queue, user_replies_queue):
        q.put(TERMINATE)
    gui.expect_m3u8_and_url[0] = TERMINATE
    gui.expect_m3u8_and_url[1] = gui.player_play_event
    gui.expect_m3u8_and_url.append(gui.scrollbar_playing_event)
    gui.player_fetching_event.set((0, 0, True))
    stream_queue.put(TERMINATE)
    sock.sock.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
