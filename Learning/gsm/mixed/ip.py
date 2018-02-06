#!/usr/bin/python
import socket, struct, fcntl
myport="eno1"
def get_ip(iface = myport):
 ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
 try:
  res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
 except Exception, e:
  return None
 ip = struct.unpack('16sH2x4s8x', res)[2]
 return socket.inet_ntoa(ip)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
SIOCGIFADDR = 0x8915
myIP=get_ip(myport)
if('10' in myIP):
 print("My IP address is '%s'"%myIP)
else:
 print("different IP")

