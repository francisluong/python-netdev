#!/usr/bin/env python

from ncclient import manager
from pprint import pprint as pp
from auth.userpass import Userpass
#for argv
import sys, os


if len(sys.argv) < 3:
    print "usage: {} <path_to_authfile> <router>".format(sys.argv[0])
    exit()

#load yaml.userpass
userpass = Userpass()
userpass.load(sys.argv[1])

#connect to router using netconf
session = manager.connect(host=sys.argv[2], port=830, username=userpass.user(),
    password=userpass.passwd(), timeout=10, hostkey_verify=False)

#get-software-information
result = session.get_software_information()
print result.tostring

#print out hostname 
hostname = result.xpath("//host-name")[0].text
print "Hostname: {}".format(hostname)

#print version string:
path = "software-information/package-information[name='junos']/comment"
version_comment = result.xpath(path)[0].text
print "Version: {}".format(version_comment)

