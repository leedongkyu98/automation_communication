from import socket*
group_addr = ("224.0.0.255",5005)
s_sock = socket(AF_INET,SOCK_DGRAM)
s_sock.settimeout(0.5)
TTL = struct.pack('@i',2)
s_sock.setsockopt(IPPROTO_IP,IP_MULTICAST_TTL,TTL)
s_sock.setsockopt(IPPROTO_IP,IP_MULTICAST_LOOP,False)
while True:
    rmsg = input("your message")
    s_sock.sendto(rmsg.encode(),group_addr)