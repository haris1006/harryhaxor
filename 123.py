import os
import re
import threading
import time

try:
    print('\harry haxor')
    time.sleep(0.5)
    import requests #call module
    print('\n<3')
    time.sleep(0.5)
except:
    os.system('pip install requests') #install module
    print('\nRev Ip will Load now')
    time.sleep(0.5)

import requests

os.system('cls' if os.name == 'nt' else 'clear') #clear terminal

s = requests.Session()

ua = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' #user gent
        }

names = []

banner = """




$$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$$\ $$\     $$\       $$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\  
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\\$$\   $$  |      $$ |  $$ |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |\$$\ $$  /       $$ |  $$ |$$ /  $$ |\$$\ $$  |$$ /  $$ |$$ |  $$ |
$$$$$$$$ |$$$$$$$$ |$$$$$$$  |$$$$$$$  | \$$$$  /        $$$$$$$$ |$$$$$$$$ | \$$$$  / $$ |  $$ |$$$$$$$  |
$$  __$$ |$$  __$$ |$$  __$$< $$  __$$<   \$$  /         $$  __$$ |$$  __$$ | $$  $$<  $$ |  $$ |$$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |          $$ |  $$ |$$ |  $$ |$$  /\$$\ $$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |          $$ |  $$ |$$ |  $$ |$$ /  $$ | $$$$$$  |$$ |  $$ |
\__|  \__|\__|  \__|\__|  \__|\__|  \__|   \__|          \__|  \__|\__|  \__|\__|  \__| \______/ \__|  \__|
                   No bugs
                   PAID | NOT FREE



"""

def reverse():
        try:
                print(banner)
                site = input('Enter your ip list ')
                line = open(site,'r').read().splitlines()
                print("")
                for site in line:
                        if site.startswith("http://"):
                                site = site.replace("http://", "")
                        if site.startswith("https://"):
                                site = site.replace("https://", "")
                        response = s.get("https://rapiddns.io/sameip/" + site + "?full=1#result", headers=ua).content.decode("utf-8")
                        pattern = r"</th>\n<td>(.*?)</td>"
                        results = re.findall(pattern, response)
                        print("2023 Priv8 Rev Ip " + site + " - [ " + str(len(results)) + " ]")

                        for line in results:
                                line = line.strip()  #delete ' '
                                if line.startswith("www."):
                                        line = "" + line[4:]
                                if line not in names:
                                        names.append(line)
                                        with open('2023Domains.txt', 'a+') as f:
                                                f.write(line + "\n") #write output

        except:
                pass

t = threading.Thread(target=reverse)
t.start()