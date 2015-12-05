#!/usr/bin/python2.7

# iter(tag=None)

#     Creates a tree iterator with the current element as the root. The
#     iterator iterates over this element and all elements below it, in
#     document (depth first) order. If tag is not None or '*', only
#     elements whose tag equals tag are returned from the iterator. If
#     the tree structure is modified during iteration, the result is
#     undefined.

#     New in version 2.7.

# iterfind(match)

#     Finds all matching subelements, by tag name or path. Returns an
#     iterable yielding all matching elements in document order.

#     New in version 2.7.

# itertext()

#     Creates a text iterator. The iterator loops over this element and
#     all subelements, in document order, and returns all inner text.

import xml.etree.ElementTree as ET

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/burp.ssl.xml'

tree = ET.parse(fname)
root = tree.getroot()

# RETURN OF ALL <severity>Information</severity> TAG TEXT FILTERING INFORMATION.
# The below works

issue = root.find('issue')

for vuln in issue.iter():
    print vuln

for rank in root.iter('severity'):
    rank = rank.text
    if rank == 'Information':
        continue
    else:
        ranking = 'rank: ' + rank

# BIG DUMB RETURN OF ALL TEXT
# for parts in root.itertext():
#     print parts

# xPATH ATTEMPT
#issues = tree.findall('.//issue')

