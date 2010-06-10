#!/usr/bin/python

import sys
import re
import string
import httplib
import urllib2
import re
import time
import mechanize

def StripTags(text):
    finished = 0
    while not finished:
        finished = 1
        start = text.find("<")
        if start >= 0:
            stop = text[start:].find(">")
            if stop >= 0:
                text = text[:start] + text[start+stop+1:]
                finished = 0
    return text


domain_name=sys.argv[1]
d={}
page_counter = 0

page_counter_web=20
try:
#	print "+ Encontre esto papacho:"+""
#	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n"+""


	# .* hace match con muchas cosas.... entonces puse [^ ]+ para que ponga todo, mientras
	# no sea un espacio,  y que termine con el domain_name (fijate en el re.escape)
	restr = 'www\.[^ ]+'+ re.escape(domain_name) +'/'
	regx  = re.compile(restr)

	br = mechanize.Browser()	
	br.set_handle_robots( False )
	br.addheaders = [('User-agent', 'Firefox')]
	br.open( "http://www.google.com.py/" )

	br.select_form( 'f' )
	br.form[ 'q' ] = "site:"+str(domain_name)
	br.submit()	
	while page_counter_web < 400 :
		for link in br.links():
			dom_webs = regx.findall(link.url)
			for dom_web in dom_webs:
			    d[dom_web]=1
			    uniq_dom_web=d.keys()
			a="/search?q=site:"+str(domain_name)+"&hl=es&ie=UTF-8&start="+str(page_counter_web)+"&sa=N"
			
			if(link.url==a):
				br.follow_link(link)
		page_counter_web = page_counter_web +10
		time.sleep(7)
			

except IOError:
    print "Opa, problemas de conexion ches"+""
for uniq_dom_web in d.keys():
	print uniq_dom_web+""
