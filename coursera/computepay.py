def computepay():
    h = raw_input('Hours per week: ')
    hrsf = float(h)
    r = raw_input('Per hour rate: ')
    ratef = float(r)
    if hrsf > 40:
    	xx = hrsf - 40
	tandh = xx * ratef * 1.5
        totalpay = tandh + (40 * 10.5)
        return totalpay
    else:
    	pay = hrsf * ratef
    	return pay

print computepay()

