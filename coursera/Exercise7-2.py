#!/usr/bin/python2.7

fname = raw_input("Enter file name: ")
fh = open(fname)
conf = 0
for line in fh:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count = 1
        for total in line:
            count = count + 1
        dspam = line
        dspam = dspam[20:]
        dspam = float(dspam)
        conf = conf + dspam
print 'Average spam confidence: ' + str(conf / count)


