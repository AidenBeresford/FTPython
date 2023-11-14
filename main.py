from client import Client
from args import args

host = args.host
port = args.port

source_host, source_port = args.src

source_address = (source_host, int(source_port))
encoding = args.encode

FTP = Client(host, port, source_address, encoding)

print(FTP.next_line(), end="")  # end="" just removes the newline that python adds

FTP.close()
