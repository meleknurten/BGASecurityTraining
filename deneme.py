#!/usr/bin/env python


import sys


def foo_out():
    print >> sys.stdout, "STDOUT"


def foo_err():
    print >> sys.stderr, "STDERR"


if __name__ == "__main__":
    foo_out()
    foo_err()


