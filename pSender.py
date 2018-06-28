#!/usr/bin/env python3

import sys, time, colorama, errno
from socket import *
from colorama import Fore

message = str(sys.argv[1])
ip = "10.0.0.255"

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:

    print(Fore.BLUE + "Sending message: ",message," with destination ",ip,end="")

    try:
        s.sendto((message+"\n").encode(), (ip, 9000))
    
    except Exception as err:
        print(Fore.RED,end="")
        if (err.errno == errno.ENETUNREACH) or (err.errno == errno.ENONET) or (err.errno == errno.ENETUNREACH) or (err.errno == errno.ENETDOWN) or (err.errno == errno.ENETRESET) :
            print("\t\t[Error] problems with the network, try again...",end="")
        else:
            raise

    else:
        print(Fore.GREEN + "\t\t[Succes]",end="")
    
    print(Fore.RESET)
 
    time.sleep(1)
