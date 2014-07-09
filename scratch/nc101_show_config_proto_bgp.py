#!/usr/bin/env python

from ncclient import manager
from pprint import PrettyPrinter
from auth.userpass import Userpass
from lxml import etree
#for argv
import sys, os


if len(sys.argv) < 3:
    print "usage: {} <path_to_authfile> <router>".format(sys.argv[0])
    exit()

#load yaml.userpass
userpass = Userpass(sys.argv[1])

#connect to router using netconf
session = manager.connect(
        host=sys.argv[2],
        port=830,
        username=userpass.user,
        password=userpass.passwd,
        timeout=10,
        device_params = {'name':'junos'},
        hostkey_verify=False)

#pretty printer
pp = PrettyPrinter(indent=4)

#assemble filter
config_filter = etree.Element("configuration")
proto = etree.Element("protocols")
config_filter.append (proto)
proto.append( etree.Element("bgp") )

#get-config
result = session.get_configuration(filter=config_filter)
print str(result)
print ""

#extract neighbor, type, and peer-as
neighbor = result.findtext(".//neighbor/name")
peeras = result.findtext(".//peer-as")
type = result.findtext(".//type").upper()
print "{} BGP Neighbor {} -- ASN: {}\n".format(type, neighbor, peeras)
