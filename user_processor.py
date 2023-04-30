AUTH_APPROVED = '200'

class UserProcessor:
    def __init__(self, login_finished_event, login_approved, input_queue):
        self.login_finished_event = login_finished_event
        self.input_queue = input_queue
        self.login_approved = login_approved


    def start(self):
        while True:
            self.process_input(self.input_queue.get())


    def process_input(self, rec_input):
        print(rec_input)
        self.login_approved[0] = rec_input == AUTH_APPROVED
        self.login_finished_event.set()
