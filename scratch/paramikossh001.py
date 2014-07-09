#!/usr/bin/python

from paramiko import SSHClient
from auth.userpass import Userpass
import os, sys

if len(sys.argv) < 3:
    print "usage: {} <path_to_authfile> <router>".format(sys.argv[0])
    exit()

#create ssh handler and read in keys
ssh = SSHClient()
keypath = os.path.expanduser('~/.ssh/known_hosts')
ssh.load_host_keys(keypath)

#load userpass file
userpass = Userpass(sys.argv[1])

#connect
host = sys.argv[2]
ssh.connect( host, username=userpass.user, password=userpass.passwd )

stdin, stdout, stderr = ssh.exec_command( 'show version' )
for line in stdout:
  print '... ' + line.strip('\n')

print "==="

stdin, stdout, stderr = ssh.exec_command( 'show chassis hardware' )
for line in stdout:
  print '... ' + line.strip('\n')

ssh.close()
