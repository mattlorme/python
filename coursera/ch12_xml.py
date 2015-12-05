#!/usr/bin/python2.7

import urllib
import xml.etree.ElementTree as ET

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_186330.xml'

page = urllib.urlopen(url).read()       #read url into var-page as string
tree = ET.fromstring(page)              #create xml tree from var-page string
counts = tree.findall('.//count')       #use Xpath to grab all <count> elements

count = 0                               #set var-count to 0 for summing
for val in counts:                      #convert to int assign value of <count> to num
    num = int(val.text)                 ##THIS SHIT## - sum the <count> values
    count = count + num
    print count


############################################################################################
############################  HOLY SHIT ....... This took forever   ########################
############################################################################################
##                                                                                        ##
##  The issue was getting the value out of the <count> element.  This is actually super   ##
##    simple once I found it,....DERP.  <element>.txt ---- grabs the text value of an     ##
##    elementself.                                                                        ##
##                                                                                        ##
############################################################################################
############################################################################################

#print len(count), type(count)
#print "".join([str(x) for x in counts]), len(counts), type(counts),

# for node in tree:
#     child = node.find('count')
#     print type(child), type(node)

# print node(type)
# count = node.find('count').text
# print type(count)
# lst = node.findall('comment/count')
# for item in lst:
#     print item

# lst = tree.findall("comment")
# print tree
# lst = bulk.findall('comment/count')

# print bulk
# print lst
# for item in lst:
#     print lst
#     print item
#     print item.find('count')

