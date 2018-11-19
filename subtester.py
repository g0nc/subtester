import requests
import threading
import sys
import socket
import time


def startTwo(ip, hostname):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        resulthttps = s.connect_ex((ip, 443))
        if resulthttps ==0:
                print('subdomain: '+str(hostname)+" found[HTTPS] !!!")
        else:
                resulthttp=s.connect_ex((ip, 80))
                if resulthttp ==0:
                        print('subdomain: '+str(hostname)+" found [HTTP] !!!")
        s.close()

def startOne(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        startTwo(ip, hostname)
    except:
        pass
        #print("subdomain: "+str(hostname)+" not resolved ;)")

def startZero():
        hostname = sys.argv[1]
        file = sys.argv[2]
        arquivo = open(file, 'r')
        linha = arquivo.readlines()
        for sub in linha:
                #hostname1 = new_sub +"."hostname
                hostname1 = str(sub.splitlines())+"."+str(hostname)
                hostname = hostname1.replace("['", "").replace("']", "")
                startOne(hostname1)
                #print(hostname)
                #print(hostname1)

t = threading.Thread(target=startZero, args=(""))
t.start()
