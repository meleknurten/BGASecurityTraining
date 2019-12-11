
import argparse

usage = "Usage: use --help for further information"
description = "Pentest"
parser = argparse.ArgumentParser(description = description, usage = usage)

service_name_list = ("test", "test2", "test3")

parser.add_argument('-p', '--project', dest = 'project', action = 'store', help = 'Project Name', required = True)
parser.add_argument('-c', '--config', dest = 'config', help = 'Configuration File',  required = True)
parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', help = 'Verbose Output', default = None)
parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

project_name = args.project
verbose = args.verbose
config_file = args.config

print config_file
