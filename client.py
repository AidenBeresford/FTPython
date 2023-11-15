import socket

FTP_PORT = 21  # default FTP port
LINE_CAPACITY = 4096  # maximum size of a line read in bytes


class Client:
    host = None
    port = None
    source_address = None
    encoding = None
    timeout = None
    file = None
    my_socket = None

    def __init__(self, host='', port=FTP_PORT, source_address=None, encoding='utf-8', timeout=socket.getdefaulttimeout()):
        self.host = host
        self.port = port
        self.source_address = source_address
        self.encoding = encoding
        self.timeout = timeout

        self._connect()

    def _connect(self):  # only called during initialization
        if self.host is not None:
            self.my_socket = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
            self.file = self.my_socket.makefile('r', encoding=self.encoding)

    def recv_line(self):
        line = self.file.readline(LINE_CAPACITY)  # 4096 is our maximum line size in bytes

        if len(line) > LINE_CAPACITY:
            print("Bytes received exceed capacity of " + str(LINE_CAPACITY) + " bytes.")

        # look for any line terminators and remove them if they exist
        if line[-2:] == '\r\n':
            line = line[:-2]
        elif line[-1:] in '\r\n':
            line = line[:-1]

        return line

    def send_line(self, line_in):
        line = line_in + "\r\n"
        line = line.encode(self.encoding)

        self.my_socket.sendall(line)

    def close(self):  # close our connection if it exists
        if self.my_socket is not None:
            try:
                self.my_socket.close()
            except:
                return 1
            else:
                return 0
