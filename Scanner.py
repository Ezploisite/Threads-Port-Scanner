#!/usr/bin/python3

import threading
import socket
import subprocess
import time
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

print (' _____ _                        _               ')         
print ('/__   \ |__  _ __ ___  __ _  __| |   ___  ___ __ _ _ __   ')
print ('  / /\/  _ \/  __/ _ \/ _` |/ _` |  / __|/ __/ _` |  _ \  ')
print (' / /  | | | | | |  __/ (_| | (_| |  \__ \ (_| (_| | | | | ')
print (' \/   |_| |_|_|  \___|\__,_|\__,_|  |___/\___\__,_|_| |_| ')
print ('')
target = input("Please enter the IP you want to scan: ")
print ('-' * 60)
print ('')

t1 = datetime.now()

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 

    try:
        con = s.connect((target, port))

        print('[\033[1;32m+\033[1;37m]',port,"\033[0mis open.")


        con.close()
    except: 
        pass

r = 1 
for x in range(1,999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(1000,1999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(2000,2999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(3000,3999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)

for x in range(4000,4999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)

for x in range(5000,5999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(6000,6999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(7000,7999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(8000,8999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)


for x in range(9000,9999): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start()

time.sleep(0.4)

sys.stdout.flush()

print ('')
print ('-' * 60)
print ('Ready for first \033[1;31mblood\033[0m!')
print ('-' * 60)

t2 = datetime.now()
total =  t2 - t1

print ('Scanning Completed in: ', total)
