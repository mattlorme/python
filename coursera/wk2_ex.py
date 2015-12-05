#!/usr/bin/python2.7

# How the fuck do you regex and change strings to int's
# in minimum ammount of code

import re

x = '/root/Documents/Python/coursera/data/wk2_text.txt'
fh = open(x)
total = 0

for line in fh:
    line = line.strip()
    lst = re.findall('[0-9]+', line)
    if len(lst) > 0:
        for num in lst:
            num = int(num)
            total = total + num
            print total
