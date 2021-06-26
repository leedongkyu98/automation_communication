import socket
port =2000
adress = ("localhost",port)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(adress)
while(True):
    msg = input('send')
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("리시브 메세지%s"%data.decode())
    
