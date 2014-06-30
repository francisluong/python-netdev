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
session = manager.connect(host=sys.argv[2], port=830, username=userpass.user(),
    password=userpass.passwd(), timeout=10, hostkey_verify=False)
result = session.get_software_information()
hostname = result.xpath("//host-name")[0].text
path = "software-information/package-information[name='junos']/comment"
version_comment = result.xpath(path)[0].text
print result.tostring
print "Hostname: {}".format(hostname)
print "Version: {}".format(version_comment)

