import sys
import urllib2
import time
import socket
socket.setdefaulttimeout(30)

sites_list=sys.argv[1]
f=open(sites_list,'r')
for line in f:
	start_time = time.time()
	print line.strip()
	request_web = urllib2.Request("http://"+line.strip())
	opener_web = urllib2.build_opener()
	try:
		headers = opener_web.open(request_web).info()
		print '>> SERVER 	:	'+str(headers.getheader('Server'))
		print '>> POWERED 	:	'+str(headers.getheader('X-Powered-By'))
		run_time = time.time() - start_time
		print '>> TIME 	:	%f sec' % run_time
	except urllib2.URLError, e:
		print '-----------------RIP-----------------'

