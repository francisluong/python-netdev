#!/usr/bin/python

###
import yaml
from pprint import pprint as pp
from sys import argv

if len(argv) < 2:
    print "Usage: {} <path_to_yaml_file>".format(argv[0])
    exit()

f = open(argv[1])
y1 = yaml.safe_load(f)
print yaml.dump(y1)

for task in y1[0]['tasks']:
    print " - name: {}".format(task['name'])

