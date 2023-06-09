CHUNK_SIZE = 256
SUB_LIST = [b'@', b'\r\n\r\n']
END_OF_HEADERS = b'\r\n\r\n'
SUFFIX = b'@'
HTTP = b'HTTP'
NOT_HTTP = b'LEN '
LENGTH = b'\r\nContent-Length: '
ENDLINE = b'\r\n'
REGULAR_PREFIX = 'length='


class SocketWrapper:
    """
    Wrapper for socket that admits only one message from server at a time.
    """
    def __init__(self, sock):
        """
        initialize wrapper.
        :param sock:
        """
        self.sock = sock
        self.buffer = bytearray()


    def receive_until(self, sub_list):
        """
        Receive from socket until first appearence of any string from sub_list and add to buffer.
        :param sub_list: (list(bytes)) list of substring to receive until.
        :return: None
        """
        datalist = bytearray()
        prev_chunk = b''
        curr_chunk = bytes(self.buffer)
        while True:
            relevant = (prev_chunk + curr_chunk)
            ind, sub = first(relevant, sub_list)
            if ind != -1:
                datalist.extend(relevant[:ind])
                value = bytes(datalist)
                self.buffer = bytearray(relevant[ind+len(sub):])
                return value, sub
            datalist.extend(prev_chunk)
            prev_chunk = curr_chunk
            curr_chunk = self.sock.recv(CHUNK_SIZE)


    def receive_bytes(self, n):
        """
        Receive and return n bytes.
        :param n: (int) number of bytes to receive
        :return: (bytes) bytes received.
        """
        if len(self.buffer) >= n:
            value = self.buffer[:n]
            self.buffer = self.buffer[n:]
            return value
        curr_chunk = self.sock.recv(CHUNK_SIZE)
        while len(self.buffer) + CHUNK_SIZE < n:
            self.buffer.extend(curr_chunk)
            curr_chunk = self.sock.recv(CHUNK_SIZE)
        remainder = n - len(self.buffer)
        self.buffer.extend(curr_chunk[:remainder])
        value = bytes(self.buffer)
        self.buffer = bytearray(curr_chunk[remainder:])
        return value


    def recv(self):
        """
        Receive a single message from server.
        :return: (bytes) message received.
        """
        prefix = self.receive_bytes(len(HTTP))
        if prefix == NOT_HTTP:
            return self.process_regular()
        elif prefix == HTTP:
            return self.process_http()
        else:
            raise Exception(f'SocketWrapper could not identify proper prefix/suffix. prefix/suffix was: {prefix}')


    def process_http(self):
        """
        Process and return entire http message from server.
        :return: (bytes) entire http message received.
        """
        headers, sub = self.receive_until([END_OF_HEADERS])
        http_msg = bytearray(HTTP + headers + END_OF_HEADERS)
        content_length_and_on = headers[headers.find(LENGTH) + len(LENGTH):]
        content_length = int(content_length_and_on[:content_length_and_on.find(ENDLINE)].decode())
        http_msg.extend(self.receive_bytes(content_length))
        return bytes(http_msg)


    def process_regular(self):
        """
        Process and return non-http message from server.
        :return: (bytes) message received
        """
        length_string, sub = self.receive_until([SUFFIX])
        msg = self.receive_bytes(int(length_string.decode()))
        return msg

    def send(self, data):
        self.sock.send(data)


def first(st, sub_lst):
    """
    Return index of first character of first string from sub_list appearing in st.
    :param st: (bytes)
    :param sub_lst: (bytes)
    :return: (int) index described above)
    """
    ind = -1
    first_sub = b''
    for sub in sub_lst:
        curr_ind = st.find(sub)
        if curr_ind != -1 and (curr_ind < ind or ind == -1):
            ind = curr_ind
            first_sub = sub
    return ind, first_sub


class TestSocket:
     def __init__(self, st):
             self.st = st
     def recv(self, n):
             value = self.st[:n]
             self.st = self.st[n:]
             return value


def main():
    sock = TestSocket(b'hey@hello@HTTP\r\nsvbwlihvbliae\r\nklhcbealhs c\r\nContent-Length: 14\r\nwiehbvwuovbevc\r\n\r\nabcdefghijklmnHTTP\r\nsvbwlihvbliae\r\nklhcbealhs c\r\nContent-Length: 14\r\nwiehbvwuovbevc\r\n\r\nabcdefghijklmnhello@')
    wrapper = SocketWrapper(sock)
    for i in range(5):
        print(wrapper.recv())


if __name__ == '__main__':
    main()
