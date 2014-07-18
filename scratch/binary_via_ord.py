#!/usr/bin/env python

from sys import argv


if len(argv) < 2:
    print "usage: {} <binary_value>".format(argv[0])
    exit()

binary = str(argv[1])
original = binary

i = 0
while binary != '':
    i = (i << 1)+ (ord(binary[0]) - ord('0'))
    binary = binary[1:]

print "Binary: {} --> Integer: {}".format(original, i)
