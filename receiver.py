from struct import unpack


INPUT_RECV_SIZE = 5000

class Receiver:
    def __init__(self, receive_input, input_pass_queue):
        self.receive_input = receive_input
        self.input_pass_queue = input_pass_queue


    def start(self):
        while True:
            try:
                current = self.receive_input()
                self.input_pass_queue.put(current)
            except ConnectionAbortedError:
                return
            except OSError:
                return
