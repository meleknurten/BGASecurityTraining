#!/usr/bin/python

import sys

if not len(sys.argv) == 4:
    print >> sys.stderr, "Usage: <rakam rakam islem>"
    sys.exit(1)

islem_tablosu = ("toplama", "carpma", "bolme", "cikarma")

rakam_1 = int(sys.argv[1])
rakam_2 = int(sys.argv[2])
islem = sys.argv[3]


if not islem in islem_tablosu:
    print >> sys.stderr, "islem: {0} isn't supported".format(islem)
    sys.exit(2)

def toplama(rakam1, rakam2):
    return rakam1 + rakam2


def cikarma(rakam1, rakam2):
    return rakam1 - rakam2


def carpma(rakam1, rakam2):
    return rakam1 * rakam2


def bolme(rakam1, rakam2):
    return rakam1 / rakam2

islem_tablosu2 = { "toplama":toplama, "cikarma":cikarma, "carpma":carpma, "bolme":bolme }

print islem_tablosu2[islem](rakam_1, rakam_2)

for key,val in islem_tablosu2.iteritems():
    print key, val





