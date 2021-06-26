import socket
BUFFERSIZE= 1024
port =2000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = input("메세지")
sock.sendto(msg.encode(),('localhost',port))
data , addr = sock.recvfrom(BUFFERSIZE)
print(data.decode())