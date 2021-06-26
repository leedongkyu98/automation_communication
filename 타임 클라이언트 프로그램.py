import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
adress = ("localhost",2000)
sock.connect(adress)
print("현재시간:" ,sock.recv(1024).decode())
