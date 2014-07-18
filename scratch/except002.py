#!/usr/bin/env python

from auth.userpass import Userpass
userpass = Userpass()
userpass.add_user_passwd("user1","passwd1")
userpass.add_user_passwd("user2","passwd2")

if "user3" in userpass.keys():
    print "Yes!"
else:
    print "No!"

userpass.user = "user2"
userpass.user = "user3"
