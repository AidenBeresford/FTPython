import sys
import socket

MAGIC_NUM = 0x1
FTP_PORT = 21

file = None
welcome = None
source_address = None

encoding = 'utf-8'

host = ''
port = FTP_PORT
timeout = socket.getdefaulttimeout()

mySocket = socket.create_connection((host, port), timeout, source_address)

mySocket.close()
