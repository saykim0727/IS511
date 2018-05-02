import requests
import re
from bs4 import BeautifulSoup
url_file = "live.txt"
req=""
html=""
count=0
result=""
head="['"+'"]'
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
			ff = open("result.txt","a+")
			try: 
	        	        result = re.split('key\s*=\s*'+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%40s   %s\n"%(url, result[0])
				print pval
	        	        ff.write(pval)
			except:
				check+=1
			try:
	        	        result = re.split("Anonymous\("+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%40s   %s\n"%(url, result[0])
				print pval
	        	        ff.write(pval)
			except:
				check+=1
			try:
	        	        result = re.split('User\('+head,temp)
        	        	result = re.split(head,result[1])
				pval = "%40s   %s\n"%(url, result[0])
				print pval
	        	        ff.write(pval)
			except:
				check+=1
			if check==3:
				print url+"   haven't value"
			ff.close()
			fff = open("domain.txt","a+")
			fff.write(url+"\n")
			fff.close()
		except:
			print url+"   domain not valid"
			continue

print count
