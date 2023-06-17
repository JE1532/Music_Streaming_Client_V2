import sys


TERMINATE = 'exit!'


def sender(send_queue, sock):
    """
    Runs Sender thread. Blocks.
    :param send_queue: (Queue) queue of messages to send to server.
    :param sock: (socket.socket or compatible with recv(bufsize) and send(data)) socket to send messages through.
    :return:
    """
    while True:
        data = send_queue.get()
        if data == TERMINATE:
            sys.exit(0)
        sock.send(data)
