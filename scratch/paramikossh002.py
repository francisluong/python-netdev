#!/usr/bin/python

from paramiko import Transport, Channel
from userpass import Userpass
import os, sys, datetime
import time
import re
from sys import stdout



if len(sys.argv) < 3:
    print "usage: {} <path_to_authfile> <router>".format(sys.argv[0])
    exit()

#load userpass file
userpass = Userpass(sys.argv[1])
router = sys.argv[2]

#known hosts
keypath = os.path.expanduser('~/.ssh/known_hosts')

class PSession(object):
    """Wrapper for Paramiko Transport and Channel for Expect-like sessions"""

    def __init__(self, userpass_db):
        self.user = userpass_db.user
        self.passwd = userpass_db.passwd
        self.received_text = ""
        self.prompt_re = "([a-z]+@[a-zA-Z0-9\.\-\_]+[>#%])"
        self._timeout_sec = 10

    def connect(self, hostname_address):
        self._transport = Transport(hostname_address)
        self._transport.connect(username=userpass.user, password=userpass.passwd)
        self.ssh_channel = self._transport.open_channel("session")
        self.pty = self.ssh_channel.get_pty()
        self.ssh_channel.invoke_shell()
        self.wait_for_prompt()
        session.send("set cli screen-length 0")

    def txrx_status(self):
        chan = self.ssh_channel
        return "Send Ready: {}, Receive Ready: {}".format(chan.send_ready(), chan.recv_ready())

    @property
    def timeout(self):
        return self._timeout_sec

    @timeout.setter
    def timeout(self, new_timeout_sec):
        self._timeout_sec = new_timeout_sec

    def wait_for_prompt(self):
        return self.wait_for_regex(self.prompt_re)

    def wait_for_regex(self, expression):
        chan = self.ssh_channel
        done = False
        start_time = time.clock()
        while ((time.clock() - start_time) <= self.timeout) and not done:
            time.sleep(0.1)
            if chan.recv_ready():
                outbuffer = chan.recv(1024)
                if re.search("\n",outbuffer):
                    start_time = time.clock()
                self.received_text = self.received_text + outbuffer
                stdout.write(outbuffer)
                stdout.flush()
            else:
                outbuffer = ""
            done = re.search(expression, outbuffer)
        if not done:
            raise hell

    def _sendline(self, line):
        chan = self.ssh_channel
        if chan.send_ready():
            chan.send(line.strip() + "\n")
        else:
            raise hell

    def send(self, textblock):
        configtext = textblock.strip()
        for line in textblock.splitlines():
            self._sendline(line)
            self.wait_for_prompt()



#create ssh handler and read in keys
session = PSession(userpass)
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
