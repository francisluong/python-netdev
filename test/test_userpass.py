# python
from auth.userpass import Userpass
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class Test_Userpass(object):
    def test_userpass_001(self):
        """Check userpass vs. 2 user adds, default/first user"""
        userpass = Userpass()
        userpass.add_user_passwd("user1", "passwd1")
        userpass.add_user_passwd("user2", "passwd2")
        assert_equal( userpass.user(), "user1" )
        assert_equal( userpass.passwd(), "passwd1" )

    def test_userpass_002(self):
        """Check userpass vs. 2 user adds, switch users"""
        userpass = Userpass()
        userpass.add_user_passwd("user1", "passwd1")
        userpass.add_user_passwd("user2", "passwd2")
        userpass.change_user( "user2" )
        assert_equal( userpass.user(), "user2" )
        assert_equal( userpass.passwd(), "passwd2" )

    def test_userpass_003(self):
        """Check userpass vs. 2 user adds, keys and has_key"""
        userpass = Userpass()
        userpass.add_user_passwd("user1", "passwd1")
        userpass.add_user_passwd("user2", "passwd2")
        assert_equal( userpass.has_key("user1"), True )
        assert_equal( userpass.has_key("user2"), True )
        assert_equal( userpass.has_key("user3"), False )
        assert_equal( sorted(userpass.keys()), ["user1", "user2"] )

    def test_userpass_004(self):
        """Check userpass file load"""
        #write yaml file
        filepath = "/var/tmp/test.userpass.004.yml"
        f = open( filepath, "w")
        f.write("""
        users:
            user1: passwd1
            user2: passwd2
        defaultuser: user1
        """)
        f.close()
        #read in yaml pwdb
        userpass = Userpass()
        userpass.load( filepath )
        #perform checks per testcases above
        assert_equal( userpass.user(), "user1" )
        assert_equal( userpass.passwd(), "passwd1" )
        userpass.change_user( "user2" )
        assert_equal( userpass.user(), "user2" )
        assert_equal( userpass.passwd(), "passwd2" )
        assert_equal( userpass.has_key("user1"), True )
        assert_equal( userpass.has_key("user2"), True )
        assert_equal( userpass.has_key("user3"), False )


