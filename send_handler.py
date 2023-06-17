import sys


TERMINATE = 'exit!'


def sender(send_queue, sock):
    while True:
        data = send_queue.get()
        if data == TERMINATE:
            sys.exit(0)
        sock.send(data)
