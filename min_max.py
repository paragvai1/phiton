def myMinMax(myList = []):
	for a in myList:
		if type(a) is int:
			min = a
			max = a
			break	
		
	for b in myList:	
		if type(b) is int:
			if b<min:
				min = b
			if b>max:
				max = b

	res = [min,max]

	return res
	pass