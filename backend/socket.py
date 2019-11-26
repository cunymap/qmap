import socket
import sys
import os

addr='../../sock'

try:
    os.unlink(addr)
except OSError:
    if os.path.exists(addr):
        raise

sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(1)