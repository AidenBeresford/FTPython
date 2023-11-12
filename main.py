from client import Client

source_address = None

encoding = 'utf-8'

host = ''
port = 21

FTP = Client(host, port, source_address)
FTP.close()

del FTP
