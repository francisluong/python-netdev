#!/usr/bin/env python

from netaddr import IPAddress, IPNetwork
import pprint

#single address
ip = IPAddress("192.168.1.31")
print "ip.format(): {}".format(ip.format())
print "str(ip): {}".format(str(ip))

#netblocks
netblock = IPNetwork("192.168.1.0/24")
print "Netmask: {}".format(netblock.netmask)
print "CIDR: {}".format(netblock.cidr)
print "Broadcast: {}".format(netblock.broadcast)

#you can use list() to generate a list of ips belonging to a netblock
ip_list = list(netblock)
#and get subnets too!
list_31 = list(netblock.subnet(31))
print "list_31[:3]: {}".format(list_31[:3])

#And we can work through the list of subnets
for subnet in list_31:
    addresses = list(subnet)
    print "Addresses belonging to {}: ({} {})".format(subnet,str(addresses[0]),str(addresses[1]))
