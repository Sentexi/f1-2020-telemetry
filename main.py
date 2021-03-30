#!/usr/bin/env python3
# coding=utf-8
#
# F1 Telemetry - Main application
# Written in Python by Sentexi
#
# Receives F1 Telemetry data and makes it accessible via CLI, CSV or application
#
# This work was made possible thanks to the following sources:
# -- https://docs.python.org/3/library/struct.html
# -- https://docs.microsoft.com/de-de/cpp/cpp/data-type-ranges?view=msvc-160
# -- https://forums.codemasters.com/topic/50942-f1-2020-udp-specification/
#
#
import csv
import os
import socket, math, sys # Import libraries
from struct import * # Import everything from struct
import numpy as np #import numpy
import headers as H #import predefined header structures
import writefile as W #imports a simple csv file writer

UDP_IP = "0.0.0.0" # UDP listen IP-address (0.0.0.0 = all)
UDP_PORT = 20777 # UDP listen port
PACKET_SIZE = 9999 # Amount of bytes in packet

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP Socket
udp.bind((UDP_IP, UDP_PORT)) # Bind socket to IP and port
print ("F1 Telemetry ready") # Init message
print ("Listening on " + UDP_IP + ":" + str(UDP_PORT)) # Show IP and port

'''
disambiguation of struct keys as used in F1 2020 telemetry

uint8    unsigned char B

int8    signed char    b

uint16   unsigned short    H

int16    short    h

float    f

uint64    unsigned long long    Q

'''


#Initialize folder structure
if not os.path.isdir("session"):
    os.mkdir("session")
    
for num in range(10):
    if not os.path.isdir(os.path.join("session",str(num))):
        os.mkdir(os.path.join("session",str(num)))

# Package receival loop
while True:
    index = 0; # Set starting index
    data, addr = udp.recvfrom(PACKET_SIZE) # Receive data from UDP socket

    #receive header to know the package id
    pkg_header = unpack(H.header,data[0:24]) #array of shape (1,10) Nr. 4 is PackageID
    pkg_header = unpack(H.header,data[0:24]) #array of shape (1,10) Nr. 4 is PackageID

    if pkg_header[4] != 3:
        #print("packageID = {}, size: {} should be: {}".format(pkg_header[4],sys.getsizeof(data),calcsize(H.packages[pkg_header[4]])))
        ar = np.array(unpack(H.packages[pkg_header[4]],data)) #transforms data in numpy array
        W.write_csv(pkg_header[4],ar) #writes each package in correspondent CSV
        #print(ar)
