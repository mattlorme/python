#!/usr/bin/python2.7

# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() function.
# The program should build a list of words.
# For each word on each line
# check to see if the word is already in the list
# and if not append it to the list.
# When the program completes, sort and print the resulting
# words in alphabetical order.

fname = raw_input("Enter file name: ")
#if nothing is provided for fname use path /root....../mbox-t..
if len(fname) == 0:
    fname = '/root/Documents/Python/coursera/data/romeo.txt'

fh = open(fname)
lst = list()

for line in fh:
    line = line.strip()
    alst = line.split()
    for word in alst:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()
print lst
