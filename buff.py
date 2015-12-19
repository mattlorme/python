#!/usr/bin/python2.7

# buff overflow lunch n' learn with Justin

import socket

RHOST =
RPORT =

buf = ""
buf += "GET /index.html HTTP/1.1\r\n"
buf += "Host: {0}:{1}\r\n".format(RHOST, RPORT)
buf += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(buf)
s.close()


