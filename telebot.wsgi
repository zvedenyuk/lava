import urlparse as parse
import sys
from urllib import urlencode
from urllib import unquote
from random import randint
import json
import time
import re
import requests
import pickle
import base64
import os

TOKEN = '1234567890:XXXxxxXXXxxxXXXxxxXXXxxxXXXxxxXXXx' # PLACE YOUR TELEGRAM BOT TOKEN HERE!
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

appDir=os.path.abspath(os.path.dirname(__file__))

def fir(u):
	try:
		with open(u, 'r') as f:
			return f.read()
	except: return ""
def fiw(u,s):
	with open(u, 'w') as f:
		f.write(s)
def fia(u,s):
	with open(u, 'a') as f:
		f.write(s)


cookieFolder=appDir+"/../cookies"
if not os.path.isdir(cookieFolder):
	os.mkdir(cookieFolder)

def save_cookies(session, filename, cookieFolder):
	if filename==False:
		return False
	filename = cookieFolder+"/"+filename+".txt"
	with open(filename, 'w') as f:
		f.truncate()
		pickle.dump(session.cookies._cookies, f)

def load_cookies(session, filename, cookieFolder):
	if filename==False:
		return False
	filename = cookieFolder+"/"+filename+".txt"
	if not os.path.isfile(filename):
		return False
	with open(filename) as f:
		cookies = pickle.load(f)
		if cookies:
			jar = requests.cookies.RequestsCookieJar()
			jar._cookies = cookies
			session.cookies = jar
		else:
			return False

def curl(url,data=False,headers=False,cookie=False,multipart=False,proxy=False,onlyContent=True,timeout=40,cookieFolder=cookieFolder,method="POST"):
	#print [url,data,headers,cookie,multipart,proxy,onlyContent,timeout,cookieFolder]
	if multipart==True and data!=False:
		boundary=nonce()
		data=multipartForm(data, boundary)
		if headers==False: headers={}
		headers["Content-Type"]="multipart/form-data; boundary="+boundary
	if proxy!=False and proxy!="":
		if proxy.count("@")>0:
			proxy=proxy.split("@")
			proxy={"http": "http://"+proxy[0]+"@"+proxy[1]+"/", "https": "http://"+proxy[0]+"@"+proxy[1]+"/"}
		else:
			proxy={"http":"http://"+proxy+"/", "https":"http://"+proxy+"/"}
	s = requests.Session()
	if method=="POST":
		if data==False:
			try: r = s.get(url, headers=headers, cookies=load_cookies(s,cookie,cookieFolder), proxies=proxy, timeout=timeout)
			except: return ""
		else:
			try: r = s.post(url, data=data, headers=headers, cookies=load_cookies(s,cookie,cookieFolder), proxies=proxy, timeout=timeout)
			except: return ""
	elif method=="PUT":
		try: r = s.put(url, data=data, headers=headers, cookies=load_cookies(s,cookie,cookieFolder), proxies=proxy, timeout=timeout)
		except: return ""
	#print r.status_code
	#print r.request.headers
	#print r.headers
	save_cookies(s, cookie, cookieFolder)
	if onlyContent: return r.content
	else: return r

def application(env, start_response):	
	try:
		request_body_size = int(env.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	
	post=env['wsgi.input'].read(request_body_size)

	start_response('200 OK', [('Content-Type','text/html')])
	
	if(post!=""):
		r=json.loads(post)
		try: text=r['message']['text']
		except: return ""
		try: chatId=r['message']['chat']['id']
		except: return ""
		
		if text=="/current":
			r=fir(appDir+"/videoId.txt")
			text="Current Lava is \nhttps://youtu.be/"+str(r)
		elif text=="/list":
			text="""/current - Which Lava is current?
/list - List my favorite lavas

/wnhvanMdx4s - Set space
/aZ_rw6FDOAM - Set lava lamp
/L_LUpnjgPso - Set fireplace"""
		else:
			try: text=re.findall(".*?(?:v=|be\/|^\/)(.+?)(?:&.+?)*$",text)[0]
			except: text="Sorry, but no"
			else:
				fiw(appDir+"/videoId.txt",str(text))
			text="Changing the Lava to: /"+str(text)
		
		headers = {'Content-Type': 'application/json'}
		message = {
			'chat_id': chatId,
			'text': text
		}
		
		r=curl(API_URL,json.dumps(message),headers=headers)
	
	return ""