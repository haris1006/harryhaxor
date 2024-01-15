#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys,time,re,requests,os,base64,string,random
from multiprocessing.dummy import Pool
requests.urllib3.disable_warnings()


def error(text):
	print("[-] :"+text)
def warning(text):
	print("[*] :"+text)
def current(text):
	print("[+] :"+text)
headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}


def URLdomain(site):
	if site.startswith("http://") :
		site = site.replace("http://","")
	elif site.startswith("https://") :
		site = site.replace("https://","")
	else :
		pass
	pattern = re.compile('(.*)/')
	while re.findall(pattern,site):
		sitez = re.findall(pattern,site)
		site = sitez[0]
	return site

def Check_Alive(site):
	try:
		url = 'http://' + URLdomain(site)

		response = requests.get(url + "/.well-known/index.php" , headers=headers,  verify=False, timeout=15)
		#if 'FilesMan' in response.content:
		if 'input type="text" readonly="1" id="upload_visible"' in response.content:
			current(' -| ' + url + ' ----> is Vuln -:)')
			open('File-manager.txt','a').write(url  + "/.well-known/index.php\n")
		else:
			error(' -| ' + url + ' ---->Not Vuln  !')
			
	except Exception as ex:
		error(' -| ' + url + ' ----> is Dead  !')
def RunTool(url):
    try:
        Check_Alive(url)
    except:
        pass

try:
	target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path = str(sys.argv[0]).split('\\')
	warning('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
	#exit()
mp = Pool(150)
mp.map(RunTool, target)
mp.close()
mp.join()