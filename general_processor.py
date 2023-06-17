STREAM = 'HTTP'
USER_REQUEST = 'UserProcessor'
GUI = b'Gui'
UPLOAD_RESP = b'Upload_Resp'


TERMINATE = 'exit!'


class GeneralProcessor:
    """
    General processor - gets all server input from receiver and delivers every message to
    appropriate thread.
    """
    def __init__(self, input_pass_queue, stream_proc_queue, user_proc_queue, gui_msg_queue, upload_resp_queue):
        """
        initialize a general processor.

        :param input_pass_queue: input queue getting from receiver
        :param stream_proc_queue: queue of messages for stream processor
        :param user_proc_queue: queue of messages to user processor
        :param gui_msg_queue: queue of messages for gui
        :param upload_resp_queue: queue of upload responses (go to gui)
        """
        self.input_pass_queue = input_pass_queue
        self.stream_proc_queue = stream_proc_queue
        self.user_proc_queue = user_proc_queue
        self.gui_msg_queue = gui_msg_queue
        self.upload_resp_queue = upload_resp_queue


    def start(self):
        """
        start general processor thread. blocks and executes general processor.
        :return: None
        """
        while True:
            current = self.input_pass_queue.get()
            if current == TERMINATE:
                return  # termination protocol
            self.process_request(current)


    def process_request(self, request):
        """
        process a single request.
        :param request: request as a bytes object.
        :return: None
        """
        prefix = request[:len(STREAM)].decode()
        if prefix == STREAM:
            self.stream_proc_queue.put(request)  # message destined for stream processor
            return
        prefix = request[:len(GUI)]
        if prefix == GUI:
            self.gui_msg_queue.put(request)  # message destined for gui
            return
        prefix = request[:len(UPLOAD_RESP)]
        if prefix == UPLOAD_RESP:
            self.upload_resp_queue.put(request)  # message is an upload response (also destined for gui)
            return
        request_decoded = request.decode()
        prefix = request_decoded.split('/')[0]
        if prefix == USER_REQUEST:
            self.user_proc_queue.put(request_decoded[len(prefix) + 1:])  # message destined for user processor
