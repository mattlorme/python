#!/usr/bin/python2.7

#WITH CODE PRINTS AND DEBUG PRINTS

# counts = {'alan': 52,'brian':48,'christy':24}
# print '\t' "code = " + "counts = {'alan': 52,'brian':48,'christy':24}"
# print 'raw counts: ' + str(counts)
# lst = counts.keys()
# print '\t' "code = " + "lst = counts.keys()"
# print 'raw lst: ' + str(lst)
# lst.sort()
# print '\t' "code = " + "lst.sort()"
# print 'sorted lst: ' + str(lst)
# #print 'raw: ' + str(counts)
# print 'raw counts: ' + str(counts)
# print '\t' "code = " + "for key in lst: \n" + '\t\t' + "print str(key), str(counts[key])"
# print 'sorted dict: '
# for key in lst:
#     #print 'sorted dict: '
#     #print counts
#     print str(key), str(counts[key])


#WITH DEBUG PRINTS

# counts = {'alan': 52,'brian':48,'christy':24}
# print 'raw counts: ' + str(counts)
# lst = counts.keys()
# print 'raw lst: ' + str(lst)
# lst.sort()
# print 'sorted lst: ' + str(lst)
# print 'raw counts: ' + str(counts)
# print 'sorted dict: '
# for key in lst:
#     #print 'sorted dict: '
#     #print counts
#     print str(key), str(counts[key])

####################################################################
#################  Executing code below  ###########################
####################################################################

#PRINT ALL THE CODE BEFORE RUNNING
print '\n' +"counts = {'alan':52,'brian':48,'christy':24}"
print "lst = counts.keys()"
print "lst.sort()"
print "print 'sorted dict: "
print "for key in lst: "
print '\t' + "print repr(key), ':', repr(counts[key])" + '\n'
print '##################################################' + '\n'

counts = {'alan': 52,'brian':48,'christy':24} #declare and population dictionary
lst = counts.keys() #create list of dictionary using keys of counts
lst.sort() #sort the dictionary alphabetically based on keys
print 'Original counts Dictionary (before sorting): ' + '\n' + str(counts) + '\n' #print original dictionary for clarity of example
print 'Sorted dict: ' #print the string 'Sorted dict: as a title of the sorted dict. created in for/in loop below.'
for key in lst: #loop through list setting keys to var key
    print repr(key), ':', repr(counts[key]) #print the sorted dict
