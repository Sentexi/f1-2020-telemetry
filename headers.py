#!/usr/bin/env python3
# coding=utf-8

from struct import calcsize

header = "<HBBBBQfIBB"

#structure of package id 6
package_6_codec = "HfffBbHBBHHHHBBBBBBBBHffffBBBB"
package_6 = header + package_6_codec*22 + "IBBb"



print(calcsize(package_6))

if __name__ == "__main__":
    print("Checking package integrity")
    
    print("header: size: {}".format(calcsize(header)))
    
    print("Package 1: size: {}".format(calcsize(package_0)))
    
    print("Package 1: size: {}".format(calcsize(package_1)))