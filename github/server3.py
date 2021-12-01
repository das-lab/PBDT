'''
服务端代码之主要脚本部分。这个脚本会监听 ICMP 数据包并从句法上分析其携带的数据部分（客户端 IP 地址、客户端连接端口、连接所需密码）。接着在本地打开两个新的防火墙规则。最后调用另一个 expect 脚本，以建立和客户端之间稳定的 ssh 连接。
'''

#! /usr/bin/env python
import logging
import socket
from scapy.all import *
import re
import subprocess	# py2.4 新增模块，允许用户编写代码生成新进程，连接到它们的 input/output/error 管道，并获取它们的返回/状态码。

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def icmp_monitor_callback(pkt):
	reg = re.compile("(.*)\|(.*)\|(.*)")
	g = reg.match(pkt.load)
	if g:
		subprocess.Popen(["/sbin/iptables", "-I", "INPUT", "1","-s",g.group(1),'-j','ACCEPT'])
		subprocess.Popen(["/sbin/iptables", "-I", "OUTPUT", "1","-d",g.group(1),'-j','ACCEPT'])
		p=subprocess.call(["/root/sshtunnel.sh", g.group(1),g.group(2),g.group(3)])
	return
sniff(prn=icmp_monitor_callback, filter="icmp", store=0)		# scapy.sniff() 函数会嗅探来自空气中的数据包，prn 参数用来指定回调函数，每当符合 filter 的报文被探测到时，就会执行回调函数。有关该函数的详细信息，可以参考这篇博客：https://thepacketgeek.com/scapy-sniffing-with-custom-actions-part-1/