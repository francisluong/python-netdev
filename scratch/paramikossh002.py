#!/usr/bin/python

from psession import *
from userpass import Userpass
import os, sys, datetime




if len(sys.argv) < 3:
    print "usage: {} <path_to_authfile> <router>".format(sys.argv[0])
    exit()

#load userpass file
userpass = Userpass(sys.argv[1])
router = sys.argv[2]

#known hosts
keypath = os.path.expanduser('~/.ssh/known_hosts')




#create ssh handler and read in keys
session = PSession(userpass.user, userpass.passwd)
session.connect(router)
print session.txrx_status()
configtext = """
    configure private
    annotate system "hi\"
    show | compare
    commit
    annotate system \"\"
    show | compare
    commit and-quit
"""
session.send(configtext)
session.send("show configuration")

#ssh.load_host_keys(keypath)
