#!/usr/bin/python2.7

#10.2 Write a program to read through the mbox-short.txt
#  and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time
#  and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/Python/coursera/data/mbox-short.txt'

time = dict()
line = None
fh = open(fname)
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip()
        line = line.split()
        line = line[5]
        line = line.split(':')
        hr = line[0]
        time[hr] = time.get(hr, 0) +1

for k,v in sorted(time.items()):
    print k, v
