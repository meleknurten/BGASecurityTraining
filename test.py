#!/usr/bin/env python

import sys

etc_file = "/etc/passwd"

def foo(line):

    print line

    for line in open(etc_file, "r"):
        #print line.strip(), line[:-1]
        if line[0] == "r":
            print line.strip()


if __name__ == "__main__":
    foo("line")
    sys.exit(0)
