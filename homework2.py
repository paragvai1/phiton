import homework2_module
rezult=homework2_module.typeDefinition ([16,-17,2,78.7,False,False,{'True':True},555,12,23,42,'DD',None,None])
if type(rezult) is str:
	print('Является типом '+str(rezult))
else:
	if type(rezult) is int:
		print('Длина списка/кортежа не привышает 1')
	else:
		print('Список/кортеж сотоит из строк: '+str(rezult[0])+' шт., из чисел: '+str(rezult[1])+' шт., из дробных чисел:  '+str(rezult[2])+' шт., из типа бул. значения: '+str(rezult[3])+' шт., из словарей: '+str(rezult[4])+' шт., из типа None: '+str(rezult[5])+' шт.')

print(homework2_module.sortList([16,-17,2,78.7,False,False,{'True':True},555,12,23,42,'DD']))		