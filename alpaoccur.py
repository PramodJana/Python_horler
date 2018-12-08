import os.path
import urllib as req
import requests
webURL=req.request.urlopen('https://www.google.com/')
requ=requests.get('https://www.google.com/')

if(requ.status_code==200):
	str=webURL.read().decode()
	print(str)
else:
	print ("Invalid URL")

	
	