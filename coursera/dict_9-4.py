#!/usr/bin/python2.7

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/Python/coursera/data/mbox.txt'

email = dict()
fh = open(fname)
line = None
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        line = line.split()
        address = line[1]
        email[address] = email.get(address,0) + 1

sender = None
sent = None
for a,b in email.items():
    if sender is None or b > sent:
        sender = a
        sent = b

senderlist = email.keys()
senderlist.sort()
print 'CONTRIBUTORS: '
for x in senderlist:
    print '\t' + str(x), str(email[x])

print '\n\n        ' + '            DATA TYPES'
print '\n' + '### - ' + 'SenderList Data Type:  ' + str(type(senderlist)) + '- ###'
print '### -    ' + 'line Data Type:  ' + str(type(line)) + '    - ###'
print '### -   ' + 'email Data Type:  ' + str(type(email)) + '   - ###'  + '\n'

print 'Heaviest contributor:   ' + sender, sent

# ADDED A WHOLE BUNCH OF WONK/HACK FORMATTING FOR OUTPUT

# 9.4 Write a program to read through the
# mbox-short.txt and figure out who has the sent
# the greatest number of mail messages.
# The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent the mail.

# The program creates a Python dictionary
# that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

# BONUS - ADD AN ADDITIONAL OUTPUT FOR TOP CONTRIBUTION BY UNIVERSITY ?!?
