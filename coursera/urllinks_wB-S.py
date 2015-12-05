#!/usr/bin/python2.7

import urllib
from BeautifulSoup import *

#figure out a way to use both http:// & https://
url = raw_input('Enter: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Get all anchor tags
tags = soup('a')
for tag in tags:
    # Examin the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Content:',tag.contents[0]
    print 'Attrs:',tag.attrs
    print tag.get('href', None)
