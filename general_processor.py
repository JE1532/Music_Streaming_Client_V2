STREAM = 'HTTP'
USER_REQUEST = 'UserProcessor'
GUI = b'Gui'
UPLOAD_RESP = b'Upload_Resp'


TERMINATE = 'exit!'


class GeneralProcessor:
    def __init__(self, input_pass_queue, stream_proc_queue, user_proc_queue, gui_msg_queue, upload_resp_queue):
        self.input_pass_queue = input_pass_queue
        self.stream_proc_queue = stream_proc_queue
        self.user_proc_queue = user_proc_queue
        self.gui_msg_queue = gui_msg_queue
        self.upload_resp_queue = upload_resp_queue


    def start(self):
        while True:
            current = self.input_pass_queue.get()
            if current == TERMINATE:
                return
            self.process_request(current)


    def process_request(self, request):
        prefix = request[:len(STREAM)].decode()
        if prefix == STREAM:
            self.stream_proc_queue.put(request)
            return
        prefix = request[:len(GUI)]
        if prefix == GUI:
            self.gui_msg_queue.put(request)
            return
        prefix = request[:len(UPLOAD_RESP)]
        if prefix == UPLOAD_RESP:
            self.upload_resp_queue.put(request)
            return
        request_decoded = request.decode()
        prefix = request_decoded.split('/')[0]
        if prefix == USER_REQUEST:
            self.user_proc_queue.put(request_decoded[len(prefix) + 1:])
