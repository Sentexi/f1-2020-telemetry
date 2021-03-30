#!/usr/bin/env python3
# coding=utf-8

from struct import calcsize

'''
disambiguation of struct keys as used in F1 2020 telemetry

uint8    unsigned char B

int8    signed char    b

uint16   unsigned short    H

int16    short    h

float    f

uint64    unsigned long long    Q

'''


header = "<HBBBBQfIBB"

#structure of package id 0 = Motion
'''
Contains all motion data for player’s car – only sent while player is in control
'''
package_0_codec = "ffffffhhhhhhffffff"
package_0 = header + package_0_codec*22 + "ffffffffffffffffffffffffffffff"

#structure of package id 1 = Session
'''
Data about the session – track, time left
'''
MarshalZone = "fb"
WeatherForecastSample = "BBBbb"
package_1_codec = "BbbBHBbBHHBBBBBB"
package_1 = header + package_1_codec + MarshalZone*21 + "BBB" + WeatherForecastSample*20

#structure of package id 2 = Lap Data
'''
Data about all the lap times of cars in the session
'''
package_2_codec = "ffHHfBHHHHBHBHBfffBBBBBBBBB"
package_2 = header + package_2_codec*22

#structure of package id 3 = Event
'''
Various notable events that happen during a session
'''
#TODO: handle different events
EventDataDetails = "" 
package_3_codec = "BBBB"
package_3 = header + package_3_codec*22

#structure of package id 4 = Participants
'''
List of participants in the session, mostly relevant for multiplayer
'''
ParticipantData = "BBBBB" + "c"*48 + "B"
package_4_codec = "B"
package_4 = header + package_4_codec + ParticipantData*22

#structure of package id 5 = Car Setups
'''
Packet detailing car setups for cars in the race
'''
package_5_codec = "BBBBffffBBBBBBBBffffBf"
package_5 = header + package_5_codec*22

#structure of package id 6 = Car Telemetry
'''
Telemetry data for all cars
'''
package_6_codec = "HfffBbHBBHHHHBBBBBBBBHffffBBBB"
package_6 = header + package_6_codec*22 + "IBBb"

#structure of package id 7 = Car Status
'''
Status data for all cars such as damage
'''
package_7_codec = "BBBBBfffHHBBHBBBBBBBBBBBBBBBBBbfBfff"
package_7 = header + package_7_codec*22

#structure of package id 8 = Final Classification
'''
Final classification confirmation at the end of a race
'''
package_8_codec = "BBBBBBfdBBB" + "B"*8 + "B"*8
package_8 = header + "B" + package_8_codec*22

#structure of package id 9 = Lobby Info Packet
'''
Information about players in a multiplayer lobby
'''
package_9_codec = "BBB" + "c"*48 + "B"
package_9 = header + "B" + package_9_codec*22

dummy ="xyz"
packages = [package_0,package_1,package_2,dummy,package_4,package_5,package_6, \
package_7,package_8,package_9]




print(calcsize(package_6))

if __name__ == "__main__":
    print("Checking package integrity")
    
    print("header: size: {} should be:{}".format(calcsize(header),24))
    
    print("Package 0: size: {} should be:{}".format(calcsize(package_0),1464))
    
    print("Package 1: size: {} should be:{}".format(calcsize(package_1),251))
    
    print("Package 2: size: {} should be:{}".format(calcsize(package_2),1190))
    
    print("Package 3: size: {} should be:{}".format(calcsize(package_3),35))
    
    print("Package 4: size: {} should be:{}".format(calcsize(package_4),1213))
    
    print("Package 5: size: {} should be:{}".format(calcsize(package_5),1102))
    
    print("Package 6: size: {} should be:{}".format(calcsize(package_6),1307))
    
    print("Package 7: size: {} should be:{}".format(calcsize(package_7),1344))
    
    print("Package 8: size: {} should be:{}".format(calcsize(package_8),839))
    
    print("Package 9: size: {} should be:{}".format(calcsize(package_9),1169))