#!/usr/bin/env python
#Importing the necessary libraries
import socket
import subprocess
import sys
# Opening file to write the results
f = open("result.txt","w+")
# Clearing the shell
subprocess.call('clear', shell=True)
# Getting the file specific path from the user
filepath = str(raw_input("Enter the file specific path: "))
# Extracting The domain/sub domain names and putting them into a list    
hostnames = [sub.rstrip('\n') for sub in open(filepath)]
# Opening Hosts ip list to append the ips of domains/sub-domains into it to be compatible with the socket lib
hostsIP = []
# Errors handling :)
try:
   for host in hostnames:
       hostsIP.append(socket.gethostbyname(host))  
except KeyboardInterrupt:
    pass
except socket.gaierror:
    pass
except socket.error:
    pass
try:
    for port in (443,80):
        length = len(hostsIP)
        for i in range(length):
            remoteServerIP = hostsIP[i]  
            res_host = hostnames[i]
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP,port))
            if result == 0:
               f.write(res_host)
            else:
                print "Port {}: closed".format(port)
            sock.close()
except KeyboardInterrupt:
    pass
except socket.gaierror:
    pass
except socket.error:
    pass
