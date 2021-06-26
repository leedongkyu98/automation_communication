import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adress = ('localhost', 2000)
s.bind(adress)
s.listen(5)

while True:
    client, addr = s.accept()
    print("connection requested from", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()