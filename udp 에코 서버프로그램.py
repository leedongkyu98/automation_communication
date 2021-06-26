import socket
port = 2000
BUFERSIZE = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",port))
while True:
    data,addr = sock.recvfrom(BUFERSIZE)
    print(data.decode())
    sock.sendto(data,addr)