import socket

FTP_PORT = 21

class Client:
    host = None
    port = None
    source_address = None
    timeout = None
    my_socket = None

    def __init__(self, host='', port=FTP_PORT, source_address=None, timeout=socket.getdefaulttimeout()):
        self.host = host
        self.port = port
        self.source_address = source_address
        self.timeout = timeout

    def _connect(self):  # only called during initialization
        if self.host is not None:
            self.my_socket = socket.create_connection((self.host, self.port), self.timeout, self.source_address)

    def close(self):  # close our connection if it exists
        if self.my_socket is not None:
            self.my_socket.close()
