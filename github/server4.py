import socket

def main():
    # 建立socke连接
    shell_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # bind端口
    shell_socket.bind(("",6666))
    # listen监听 设置最大俩个连接
    shell_socket.listen(2)
    # accept 接收 发送命令
    new_shell,addr = shell_socket.accept()
    while True:
        command = input("~$")
        new_shell.send(command.encode("gbk"))
        # 显示 数据
        data = new_shell.recv(2048).decode("gbk")
        if data:
            print (data)
        else:
            break
    # 关闭连接
    new_shell.close()
    shell_socket.close()


if __name__ == '__main__':
    main()