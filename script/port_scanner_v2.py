'''
Problem: port scanner 
Author: Nidhi kumari
Date: 24/04/25
'''
import socket as sk
import sys
import os

os.system("clear")

remortHostName = input("Enter remote hostnam: ")
remoteHostIP = sk.gethostbyname(remortHostName)
port = int(input("Enter the port to be scanned: "))

print("-" * 20)
print("Scanning ports...")
print("-" * 20)

try:
    TCP_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    result = TCP_socket.connect_ex((remoteHostIP, port))
    if result == 0:
        print(f"{port} is open on host {remortHostName} with IP {remoteHostIP}")
    TCP_socket.close()
except KeyboardInterrupt:
    print("Keyboard interrupt received.")
    sys.exit()

except sk.gaierror:
    print("Host name is invalid or DNS unreachable.")
    sys.exit()

except sk.error:
    print(f"{remortHostName} you are trying to reach is down or unreachable or firewall is blocking the connection")
    
'''
Exception      | When it Happens                            |  Message in Script
socket.gaierror| Hostname canott be resolved (DNS issues)   |  Hostname could not be resolved. Exitingâ€
socket.error   | Any other socket failure (e.g., connection)|  Couldn't connect to server
'''    
