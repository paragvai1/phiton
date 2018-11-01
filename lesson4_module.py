def found_div(start = 0, end=100, div_val=6):
	return [val for val in range(start,end) if val>div_val and val%div_val == 0]
	pass
	
def my_min(*args):
	min1=args[0]
	for b in args:
		if b<min1:
			min1 = b
	return	min1
	pass			
	
def my_max(**kwargs):

	for key, value in kwargs.items():
		val=value
	
	for a in val:
		if type(a) is int:
			max=a
			break
	
	for b in val:
		if type(b) is int and b>max:
			max = b
		
	return max
	pass