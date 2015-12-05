#!/usr/bin/python2.7

#spam = 0
#while spam < 5:
#    print('Hello world!')
#    spam = spam + 1

#name = ''
#while name != 'your name':
#    print('Please type your name.')
#    name = raw_input()
#print('Thank you!')

#name = ''
#while name != True:
#    print('Please type your name.')
#    name = raw_input()
#print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: #when spam == 3 continue is executed, never reaching print()
        continue
    print('spam is ' + str(spam))
        
