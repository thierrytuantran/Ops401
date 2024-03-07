#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set a timeout value
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ") 
portno = int(input("Enter the port number: "))  # Collect a port number from the user

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  
        print("Port open")
    else:
        print("Port closed")

portScanner(portno)
