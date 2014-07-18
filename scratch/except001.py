#!/usr/bin/env python
if "user3" in {"user2": "user3pass"}:
    print "Yes!"
else:
    print "No!"

class FError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


raise FError("test")