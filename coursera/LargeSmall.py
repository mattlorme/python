+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++THIS DIDN"T WORK+++++++++++BECAUSE THERE IS NO NUMBER LESS THAN < NONE+++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def test():
#	while True:
#		try:
#			num = int(raw_input('Number plz: '))
#			break
#		except:
#			print 'That\'s not a number. Try again.'
	smallest = None
	largest = None
	while True:
		num = input('Number plz: ')
		print type(num)
		print num
		print largest
		print smallest
	>>>>>>>	if type(num) == int and num < smallest:<<<<<<<<< 
		>>>>>SMALLEST WAS SET TO NONE - THERE IS NO NUMBER < NONE<<<<<<<
			smallest = num
			print 'wow, that ' + str(smallest) + ' is small.'
		elif type(num) == int and num > largest:
			largest = num
			print 'wow, that ' + str(largest) + ' is big.'
		elif str(num) == 'done':
			print largest
			print smallest
			break
		else:
			print 'That wasn\'t a number, it will be ignored.'

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def test():
	smallest = None
	largest = None
	while True:
		num = input('Number plz: ')
		print type(num)
		print num
		print largest
		print smallest
		if num == 'done' : break
		elif type(num) == int and num < smallest:
			smallest = num
			print 'wow, that ' + str(smallest) + ' is small.'
		elif type(num) == int and num > largest:
			largest = num
			print 'wow, that ' + str(largest) + ' is big.'
		else:
			print 'That wasn\'t a number, it will be ignored.'
	print largest
	print smallest









def test():
	smallest = None
	largest = None
	while True:
		num = input('Number plz: ')
		print type(num)
		print num
		print largest
		print smallest
		if num == 'done' : break
		elif type(num) == int and num > largest:
			largest = num
			print 'wow, that ' + str(largest) + ' is big.'
		elif type(num) == int and num < largest:
			smallest = num
			print 'wow, that ' + str(smallest) + ' is small.'
		else:
			print 'That wasn\'t a number, it will be ignored.'
	print largest
	print smallest










































def test():
	smallest = None
	largest = None
	while True:
		try:
			num = input('Number plz: ')
			if num == 'done' : break
			elif type(num) == int and num > largest:
				largest = num
				print 'wow, that ' + str(largest) + ' is big.'
			else:
				smallest = num
				print 'wow, that ' + str(smallest) + ' is small.'
		except NameError:
			print 'Invalid input'			

	print 'Invalid input'	
	print largest
	print smallest
