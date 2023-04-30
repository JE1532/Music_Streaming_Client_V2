def sender(send_queue, sock):
    while True:
        data = send_queue.get().encode()
        sock.send(data)
