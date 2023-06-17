from struct import unpack


INPUT_RECV_SIZE = 5000

class Receiver:
    """
    Represents the receiver of mesages from server.
    """
    def __init__(self, receive_input, input_pass_queue):
        """
        Initialize receiver.
        :param receive_input: (function void -> bytes) parameterless function for receiving input.
        :param input_pass_queue: queue to pass server messages to.
        """
        self.receive_input = receive_input
        self.input_pass_queue = input_pass_queue


    def start(self):
        """
        Runs the receiver thread. Blocks.
        :return: None
        """
        while True:
            try:
                current = self.receive_input()
                self.input_pass_queue.put(current)
            except ConnectionAbortedError:
                return
            except OSError:
                return
