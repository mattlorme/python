#!/usr/bin/python2.7

fhand = open('/root/Documents/Python/coursera/data/mbox.txt','r')
for line in fhand:
    line = line.rstrip()
    # only search for specified string
    if not line.startswith('From:'):
        continue
    # do 'verb' with lines containing our specified string
    print line

fhand.close()
