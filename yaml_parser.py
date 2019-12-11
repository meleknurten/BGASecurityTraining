
import os
import sys
import yaml


with open("sample.yaml", 'r') as stream:
    try:
        log_file = yaml.safe_load(stream)['Log']['LogFile']
    except Exception, err:
        print "Yaml Parse ERROR: {0}".format(err)
        sys.exit(1)

    if not os.path.exists(log_file):
        print >> sys.stderr,  "File: '{0}' doesn't exists !!!".format(log_file)
        sys.exit(1)
