def sender(send_queue, sock):
    while True:
        data = send_queue.get()
        sock.send(data)
