#!/usr/bin/env python

import os
import sys

def read_file(filename):
    print " ".join([ line.split(":")[0] for line in open(filename, "r") if not line[0] == "r" ])


def is_file_exists(filename):

    try:
        open(filename, "r")
        return True
    except:
        return False


if __name__ == "__main__":
    
    if not len(sys.argv) == 2:
        print >> sys.stderr, "Usage: {0} FILE".format(sys.argv[0])
        sys.exit(1)

    passwd_file = sys.argv[1]
    
    if is_file_exists(passwd_file):
        print "OK"
    else:
        print "NOT"

    try:
        open(passwd_file, "r")
        print "OK"
    except:
        print "NOT"

    if os.path.exists(passwd_file):
        print "OK"
    else:
        print "NOT"
    
    """
    try:
        file_read = open(passwd_file, "r")
        for line in file_read:
            print line.strip()
    except Exception, err:
        print err
    finally:
        file_read.close()
    
    #read_file(passwd_file)
    """
