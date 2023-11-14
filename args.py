import argparse

FTP_PORT = 21

parser = argparse.ArgumentParser(
    prog="FTPython CLI",
    description="Sockets with a server using FTP.",
    epilog="An elegant client for a more civilized age.")

parser.add_argument('--host',
                    metavar='<host>',
                    type=str,
                    help="enter the host to be connected to",
                    default='')

parser.add_argument('--port',
                    metavar='<port>',
                    type=int,
                    help="enter the host's port to be connected to",
                    default=FTP_PORT)

parser.add_argument('--src',
                    metavar=('<host>', '<port>'),
                    nargs=2,
                    help="enter source address",
                    default=('', 0))

parser.add_argument('--encode',
                    metavar='<format>',
                    type=str,
                    help="enter the encoding format",
                    default='utf-8')

args = parser.parse_args()
