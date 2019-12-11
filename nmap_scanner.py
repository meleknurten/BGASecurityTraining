
import sys
import shlex
import argparse
import subprocess

usage = "Usage: use --help for further information"
description = "Nmap Scanner"
parser = argparse.ArgumentParser(description = description, usage = usage)

parser.add_argument('-s', '--subnet', dest = 'subnet', action = 'store', help = 'Subnet', required = True)

args = parser.parse_args()
subnet = args.subnet

cmd_list_1 = shlex.split("nmap -n -Pn -sS --top-ports 100 --open {0}".format(subnet))
cmd_list_2 = ['nmap', '-n', '-Pn', '-sS', '--top-ports', '100', '--open', subnet]

print cmd_list_1
print cmd_list_2

proc = subprocess.Popen(cmd_list_1, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
out, err = proc.communicate()

print out
