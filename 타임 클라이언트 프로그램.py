import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
adress = ("localhost",2000)
sock.connect(adress)
print("íėŽėę°:" ,sock.recv(1024).decode())
