# python
import netdev
import getpass
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class Test_NetDev(object):
    def test_netdev_ssh_001(self):
        """it..."""
        user = getpass.getuser()
        session = netdev.SSH(user)
