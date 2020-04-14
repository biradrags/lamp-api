import socket
import sys

UDP_IP = "192.168.88.236"
UDP_PORT = 8888

MESSAGE = "GET"
server_address = (UDP_IP, UDP_PORT)

# create a tcp/ip socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
    # send data
    print('sending "%s"' % MESSAGE)
    sent = sock.sendto(MESSAGE.encode(), server_address)

    #recieve response
    print('waiting to recieve')
    data, server = sock.recvfrom(4096)
    print( 'recieved "%s"' % data.decode())
finally:
    print('closing socket')
    sock.close