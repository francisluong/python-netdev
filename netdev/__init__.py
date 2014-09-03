from paramiko import Transport, Channel
from sys import stdout
import re
import time

class SSH(object):
    """Wrapper for Paramiko Transport and Channel for Expect-like sessions"""

    def __init__(self, user, passwd = ""):
        """initialize SSH wrapper but do not connect"""
        self.user = user
        self.passwd = passwd
        self.prompt_re = "([a-z]+@[a-zA-Z0-9\.\-\_]+[>#%])"
        self.reset_timeout_on_newlines = True
        self._timeout_sec = 10
        self.quiet = 0
        self.received_text = ""

    def connect(self, hostname_address):
        """connect to SSH target using paramiko Transport/Channel"""
        self._transport = Transport(hostname_address)
        self._transport.connect(username=self.user, password=self.passwd)
        self.ssh_channel = self._transport.open_channel("session")
        self.pty = self.ssh_channel.get_pty()
        self.ssh_channel.invoke_shell()
        self.wait_for_prompt()
        self.ssh_channel.send("set cli screen-length 0")

    def txrx_status(self):
        """returns send and receive status as string formatted for screen"""
        chan = self.ssh_channel
        return "Send Ready: {}, Receive Ready: {}".format(chan.send_ready(), chan.recv_ready())

    @property
    def timeout(self):
        """timeout_sec getter"""
        return self._timeout_sec

    @timeout.setter
    def timeout(self, new_timeout_sec):
        """timeout_sec setter"""
        self._timeout_sec = new_timeout_sec

    def wait_for_prompt(self):
        """call self.wait_for_regex using self.prompt_re as argument"""
        return self.wait_for_regex(self.prompt_re)

    def wait_for_regex(self, expression, wait_sec=0.1):
        """
            Loop receive and wait until a regular expression is matched in output
             - raise an exception if we hit the timeout
        """
        chan = self.ssh_channel
        done = False
        start_time = time.clock()
        while ((time.clock() - start_time) <= self.timeout) and not done:
            time.sleep(wait_sec)
            if chan.recv_ready():
                while chan.recv_ready():
                    this_receive = chan.recv(1024)
                    self.received_text = self.received_text + this_receive
                    # print to screen if quiet is not set
                    if not self.quiet:
                        stdout.write(this_receive)
                        stdout.flush()
                # reset the start_time if we encounter newlines and self.reset_timeout_on_newlines is True
                if re.search("\n",self.received_text) and self.reset_timeout_on_newlines:
                    start_time = time.clock()
            #else:
                #if not chan.recv_ready, then do nothing
            done = re.search(expression, self.received_text)
        # if done is not True at this point, we consider it to be a timeout action
        if not done:
            raise NetDevError("Timeout waiting for expression match: '{}'".format(expression))
        else:
            return self.received_text

    def _sendline(self, line):
        """send a single line"""
        chan = self.ssh_channel
        if chan.send_ready():
            chan.send(line.strip() + "\n")
        else:
            raise NetDevError("Attempted to send when send not ready")

    def send(self, textblock):
        """work through a textblock and send one line at at time"""
        configtext = textblock.strip()
        for line in textblock.splitlines():
            self._sendline(line)
            self.received_text = ""
            self.wait_for_prompt()
        self.received_text = ""

class NetDevError(Exception):
    """Error class for NetDev"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
