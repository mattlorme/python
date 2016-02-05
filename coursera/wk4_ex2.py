#!/usr/bin/python2.7

# In this assignment you will write a Python program
# that expands on http://www.pythonlearn.com/code/urllinks.py.
# The program will use urllib to read the HTML from the
# data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position
# relative to the first name in the list, follow that link
# and repeat the process a number of times and report
# the last name you find.

# We provide two files for this assignment.
# One is a sample file where we give you the name for
# your testing and the other is the actual data you
# need to process for the assignment

#     Sample problem: Start at http://pr4e.dr-chuck.com/tsugi/mod
#     /python-data/data/known_by_Fikret.html Find the link at position
#     3 (the first name is 1). Follow that link. Repeat this process 4
#     times. The answer is the last name that you retrieve. Sequence
#     of names: Fikret Montgomery Mhairade Butchi Anayah Last name in
#     sequence: Anayah

#     Actual problem: Start at: http://pr4e.dr-
#     chuck.com/tsugi/mod/python-data/data/known_by_Malik.html Find
#     the link at position 18 (the first name is 1). Follow that link.
#     Repeat this process 7 times. The answer is the last name that
#     you retrieve. Hint: The first character of the name of the last
#     page that you will load is: T

# Strategy

# The web pages tweak the height between the links and hide the page
# after a few seconds to make it difficult for you to do the
# assignment without writing a Python program. But frankly with a
# little effort and patience you can overcome these attempts to make
# it a little harder to complete the assignment without writing a
# Python program. But that is not the point. The point is to write a
# clever Python program to solve the program.

# Sample execution

# Here is a sample execution of a solution:

# $ python solution.py
# Enter URL: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Montgomery.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Mhairade.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Butchi.html
# Last Url: http://pr4e.dr-chuck.com/ ... /known_by_Anayah.html


import urllib
from BeautifulSoup import *

#figure out a way to use both http:// & https://
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Malik.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Get all anchor tags
tags = soup('a')
i = 0
#loop thru <a> tags assigning each to 'tag'.  Use i to 'count' and increment
#each time through loop.
for tag in tags:
    #check value of i and get [17]'nth <a> until 7th page.
    if i < 7:
        i = i + 1
        url = tags[17].get('href', None)
    #break out of loop when i > 7
    else:
        break
    #open new 'url' and read it into var html;
    #then BS parse it into var soup
    #dig for <a> tags then back
    #to top of for loop to retreive [17]
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print i, url
