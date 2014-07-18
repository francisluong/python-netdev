#!/usr/bin/env python

from sys import argv

if __name__ == "__main__":
    print "FILE: '{}'".format(__file__)
    print argv[0] == __file__
