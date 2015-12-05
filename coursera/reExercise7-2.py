#!/usr/bin/python2.7

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/Python/coursera/data/mbox-short.txt'

#read text from file into fh
fh = open(fname)
conf = 0

#loop thru file selecting only lines beginning with 'X-DSP...etc.'
for line in fh:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count = 1
        for total in line:
            count = count + 1 #set count to 1 and add 1 for each \n
        line = float(line[20:]) #convert to float and slice from x:end
        conf = conf + line #set conf = x.xxx from line and add iteratively

print 'Average spam confidence: ' + str(conf / count) #calc avg.

#=======================================================+
#                       TO ADD
# Prompt for string - customize ('X-DSPAM-Confid...etc.')
# Find start of string without having file
# Allow for embedded string as opposed to .startswith()
# Try/Except on user input(s)
#
#
#
#
#
#
#
