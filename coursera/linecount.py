#!/usr/bin/python2.7

xfile = open('/root/Documents/Python/coursera/data/mbox.txt','r')
linecount = 0
for line in xfile:
    linecount = linecount + 1

print 'The file has ' + str(linecount) + ' lines'
xfile.close()


