def typeDefinition (arg):
	str1=0
	num=0
	boole=0
	dic=0
	fl=0
	non=0
	if type(arg) is tuple or type(arg) is list:
			if len(arg) > 1 :
				for a in arg:
					if type(a) is str:
						str1 += 1				
			
					if type(a) is int:
						num += 1
					
					if type(a) is bool:
						boole += 1				
			
					if type(a) is dict:
						dic += 1
                    
					if type(a) is float:
						fl += 1
					
					if a is None:
						non += 1
			else:
				return 1
				pass
	else:
		if type(arg) is str:
			return 'str'
			pass
		if type(arg) is int:
			return 'int'
			pass		
		if type(arg) is bool:
			return 'bool'				
			pass
		if type(arg) is dict:
			return 'dict'
			pass        
		if type(arg) is float:
			return 'float'
			pass		
		if arg is None:
			return 'None'
			pass
	rez=[str1,num,fl,boole,dic,non]
	return rez
	pass

def sortList (arg):
	print(arg)
	mylist=[]
	for a in arg:
		if type(a) is int or type(a) is float:
			mylist.append(a)
	
	n = 1 
	while n < len(mylist):
		for i in range(len(mylist)-n):
			if mylist[i] > mylist[i+1]:
				mylist[i],mylist[i+1]=mylist[i+1],mylist[i]
		n += 1
	return mylist