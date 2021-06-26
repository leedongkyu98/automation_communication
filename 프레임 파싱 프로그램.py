'''메세지를 5문자의 페이로드를 갖는 프레임으로 구성하고 에코 서버로 전송'''

import socket
import capsule
SIZE = 5
sock = sock.socket()
sock.connect(('loacalhost',2000))

HEAD =  0x05 # 시작문자
addr = 1
seqNO = 1
frame_seq = ""
msg = "hello world"
print("전송 메세지",msg)
