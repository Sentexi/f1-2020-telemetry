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
package_7 = header + package_6_codec*22


dummy ="xyz"
packages = [package_0,dummy,dummy,dummy,dummy,dummy,package_6, \
package_7,dummy,dummy]




print(calcsize(package_6))

if __name__ == "__main__":
    print("Checking package integrity")
    
    print("header: size: {}".format(calcsize(header)))
    
    print("Package 6: size: {}".format(calcsize(package_6)))
    
    print("Package 7: size: {}".format(calcsize(package_7)))