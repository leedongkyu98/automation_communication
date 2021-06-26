import socket
print(socket.getservbyname('ftp','tcp'))
print(socket.getservbyname('http','tcp'))

print(socket.getservbyport(80))



print(socket.getprotobyname('udp'))