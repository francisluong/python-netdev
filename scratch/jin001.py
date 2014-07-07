#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

interfaces = {}
interfaces["cisco"] = "gi1"
interfaces["juniper"] = "ge-0/0/0"
print "=" * 3
for vendor in interfaces:
    template_name = vendor + ".txt"
    template = env.get_template(template_name)
    interface = interfaces[vendor]
    print template.render(intfname=interface,intfip="172.16.1.1",intfmask="255.255.255.0",intfcidr="31")
    print "==="
