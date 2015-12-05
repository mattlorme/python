#!/usr/bin/python2.7

import urllib
import re

url = 'http://' + raw_input('Enter (example format: www.google.com): ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
    print link
