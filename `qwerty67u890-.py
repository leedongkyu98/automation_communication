from socket import*
port =2500
BUFSIZE = 1024
sock = socket(AF_INET,SOCK_STREAM)
sock.bind(('localhost',2000))
sock.listen(1)
conn,(remotehost,remoteport) = sock.accept()
while True:
    data = conn.recv(BUFSIZE)
    if not data:#data = "" 상대방 소켓이 close될때
        break
    print("Recieved message:",data.decode())
    conn.send(data)
conn.close()
    
    