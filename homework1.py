import min_max 

res = [x for x in range (100) if x % 6 ==0]
print(res)

myList = [1,10, 'Dima' , 12, True, 'Oleg', 222,-3,0,1000]

print('Minimum = '+str(min_max.myMinMax(myList)[0]))
print('Maximum = '+str(min_max.myMinMax(myList)[1]))