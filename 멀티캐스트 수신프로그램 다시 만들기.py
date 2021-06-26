from socket import*
group_addr = "224.0.0.255"
import strut
r_sock = socket(AF_INET,SOCK_DGRAM)
r_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#주소 재사용
r_sock.bind(("",5005))

mreq = struct.pack("4sl",inet_aton(group_addr),INADDR_ANY)
r_sock.setsockopt(IPPROTO_IP,IP_ADD_MEMBERSHIP,mreq)
print("READy to receieve")
while True:
    rmsg, addr = r_sock.recvfrom(1024)
    print("recieve{} from ({},{})").format(rmsg.decode(),*addr)
    r_sock.sendto('ACK'.encode(),addr)