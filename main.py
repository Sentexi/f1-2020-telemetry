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
import argparse

parser = argparse.ArgumentParser(description='Records telemetry data from the Codemasters game F1 2020')

parser.add_argument('-s', type=str, default="session", help='Session folder name, default=session',required=False)
#parser.add_argument('-v', action='store_true', help='Verbose') #TODO: Add verbosity
parser.add_argument('-p', type=int, default="20777", help='UDP Port to listen to')
parser.add_argument('--ip', type=str, default="0.0.0.0", help='IP to listen for UDP Packets, defaults to all IPs')


args = parser.parse_args()


UDP_IP = args.ip #UDP listen IP-address (default: 0.0.0.0 = all)
UDP_PORT = args.p #UDP listen port default: 20777
PACKET_SIZE = 9999 # Amount of bytes in packet
sessionname = args.s #Define session name, default: session

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP Socket
udp.bind((UDP_IP, UDP_PORT)) # Bind socket to IP and port
print ("F1 Telemetry ready") # Init message
print ("Listening on " + UDP_IP + ":" + str(UDP_PORT)) # Show IP and port
print ("Session name: " + args.s)

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
if not os.path.isdir(sessionname):
    os.mkdir(sessionname)
    
for num in range(10):
    if not os.path.isdir(os.path.join(sessionname,str(num))):
        os.mkdir(os.path.join(sessionname,str(num)))

# Package receival loop
while True:
    index = 0; # Set starting index
    data, addr = udp.recvfrom(PACKET_SIZE) # Receive data from UDP socket

    #receive header to know the package id
    pkg_header = unpack(H.header,data[0:24]) #array of shape (1,10) Nr. 4 is PackageID
    pkg_header = unpack(H.header,data[0:24]) #array of shape (1,10) Nr. 4 is PackageID

    if pkg_header[4] == 4:
        #A mediocre solution for decoding the weird mess of UTF-8, int and float in a 
        #somehow civilised manner
        unpacked = unpack(H.packages[pkg_header[4]],data)
        new = []
        for i in range(len(unpacked)):
            try:
                new.append(unpacked[i].decode('utf-8').replace('\x00', ''))                 
            except:
                try:
                    new.append((unpacked[i]+unpacked[i+1]).decode('utf-8'))
                except:
                    new.append(unpacked[i])                            
        #ar = np.array(new) #transforms data in numpy array
        #print(ar)
        W.write_csv(pkg_header[4],new ,sessionname) #writes each package in correspondent CSV

    if pkg_header[4] != 3 and pkg_header[4] != 4:
        #print("packageID = {}, size: {} should be: {}".format(pkg_header[4],sys.getsizeof(data),calcsize(H.packages[pkg_header[4]])))
        ar = np.array(unpack(H.packages[pkg_header[4]],data)) #transforms data in numpy array
        W.write_csv(pkg_header[4],ar,sessionname) #writes each package in correspondent CSV
        #print(ar)
