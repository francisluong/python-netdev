#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
from netaddr import IPNetwork, IPAddress

network = IPNetwork("172.16.1.0/24")
subnets = [str(subnet) for subnet in list(network.subnet(31))[:10]]
interfaces = ["ge-0/0/{}".format(x) for x in range(10)]

template_name = "manyj.txt"
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(template_name)
print template.render(sub_ifs=zip(subnets,interfaces))
