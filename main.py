from client import Client
from args import args

host = args.host
port = args.port

source_host, source_port = args.src

source_address = (source_host, int(source_port))
encoding = args.encode

FTP = Client(host, port, source_address, encoding)

print(FTP.recv_line())
FTP.send_line('PWD')

close_resp = FTP.close()  # 0 is regular, 1 is irregular

print("Socket closed with return code " + str(close_resp))
