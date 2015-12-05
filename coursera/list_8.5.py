#!/usr/bin/python2.7

# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out
# the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

# Hint: make sure not to include the lines that start with 'From:'.

import re

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/Python/coursera/data/mbox-short.txt'

fh = open(fname)
lst = list()
count = 0

for line in fh:
    line = line.strip()
    if not line.startswith('From '):
        continue
    else:
        count = count + 1
        lst = line.split()
        print lst[1]

print 'There were ' + str(count) + ' lines in the file with From as the first word.'
