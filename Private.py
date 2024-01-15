#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
Cyan = '\033[36m'
white = '\033[37m'
black = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")

def logo():
    clear = "\x1b[0m"
    colors = [34, 32, 36, 35, 31, 37]

    x = """
         Random IP GRABBER Laravel
                                                                                                                                                                                 
   1-Grab list Of IPS
   
   
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

choice = raw_input('\033[32mChoose Number ')

def revsip1():
	Shinn = raw_input('Start At Page "1":')
	Codde = raw_input('Stop At Page: ')
	try:
		Head={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(Shinn), int(Codde)):
			UrlWebs = 'http://bitverzo.com/recent_ip?p='+str(page)
			Shin = requests.get(UrlWebs, headers=Head, timeout=15).content
			if 'Recent IP reviews' in Shin:
				Shine = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', Shin)
				for xxx in Shine:
					Repshin = xxx.replace('http://bitverzo.com/ip/', '')
					print('[+]' + Fore.GREEN + Repshin + Fore.WHITE)
					open('Ips.txt', 'a').write(Repshin+'\n')
				else:
					print(Fore.BLUE + 'Laravel + IpS' + Fore.WHITE)
	except:
		pass


def IpS():
	Shinn = raw_input('Start from page "1": ')
	Codde = raw_input('Stop At Page: ')
	try:
		Head={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(Shinn), int(Codde)):
			UrlWebs = 'http://bitverzo.com/recent_ip?p='+str(page)
			Shin = requests.get(UrlWebs, headers=Head, timeout=15).content
			if 'Recent IP reviews' in Shin:
				Shine = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', Shin)
				for xxx in Shine:
					Repshin = xxx.replace('http://bitverzo.com/ip/', '')
					print('[+]' + Fore.GREEN + Repshin + Fore.WHITE)
					open('Ips3.txt', 'a').write(Repshin+'\n')
				else:
					print(Fore.BLUE + 'Method' + Fore.WHITE)
	except:
		pass

def Main():
	try:
		if choice =='1':
			IpS()
		if choice =='2':
			revsip1()

	except:
		pass		


if __name__ == '__main__':
	Main()
