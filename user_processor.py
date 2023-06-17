AUTH_APPROVED = '200'


TERMINATE = 'exit!'


class UserProcessor:
    """
    Runs UserProcessor thread. Blocks.
    """
    def __init__(self, login_finished_event, login_approved, input_queue):
        """
        Initialize user processor.
        :param login_finished_event: event for this instance to trigger when it has finished a login (successful or failed)
        :param login_approved: (list(bool)) with 1 item indicating login success.
        :param input_queue: (Queue) queue of messages from server.
        """
        self.login_finished_event = login_finished_event
        self.input_queue = input_queue
        self.login_approved = login_approved


    def start(self):
        """
        Runs UserProcessor thread. Blocks.
        :return:
        """
        while True:
            req = self.input_queue.get()
            if req == TERMINATE:
                return
            self.process_input(req)


    def process_input(self, rec_input):
        """
        Process singls login request response and respond to it.
        :param rec_input:
        :return:
        """
        print(rec_input)
        self.login_approved[0] = rec_input == AUTH_APPROVED
        self.login_finished_event.set()
