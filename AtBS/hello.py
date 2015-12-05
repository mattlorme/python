#!/usr/bin/python2.7
# This program says hello and asks for my name

print('Hello world!')

print('What is your name?') # ask for a name
myName = raw_input()
print ('It\'s good to mee you, ' + myName)
print ('The length of your name is:')
print(len(myName))

print('What is your age?') # ask for their age
myAge = raw_input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')
