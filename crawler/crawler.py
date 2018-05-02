import requests
import re
from bs4 import BeautifulSoup
import signal
import sys
import os
url_file = "live.txt"
req=""
html=""
count=0
result=""
head="['"+'"]'

def handler(signum,frame):
	global fff
	global ff
	fff.close()
	ff.close()
	os._exit(0)

signal.signal(signal.SIGTSTP,handler)
ff = open("result.txt","a+")
fff = open("domain.txt","a+")
with open(url_file,"r") as f:
        while 1:
                url = f.readline()
                if not url:
                        break
                try:
			check = 0
			url = ("http://"+url).strip()
			#url = "http://pagez.kr/x.js"
                        req = requests.get(url)
                        count+=1
	                html = req.text
        	        soup = BeautifulSoup(html, 'html.parser')
                	temp=str(soup)
			try: 
	        	        result = re.split('key\s*=\s*'+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%-80s   %-s\n"%(url, result[0])
				print pval[:-1]
	        	        ff.write(pval)
			except:
				check+=1
			try:
	        	        result = re.split("Anonymous\("+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%-80s   %-s\n"%(url, result[0])
				print pval[:-1]
	        	        ff.write(pval)
			except:
				check+=1
			try:
	        	        result = re.split('User\('+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%-80s   %-s\n"%(url, result[0])
				print pval[:-1]
	        	        ff.write(pval)
			except:
				check+=1
			if check==3:
				pval = "%-80s   %-s\n"%(url,"haven't value")
				print pval[:-1]
			fff.write(url+"\n")
		except:
			pval = "%-80s   %-s\n"%(url,"domain not valied")
			print pval[:-1]
			continue

print count
