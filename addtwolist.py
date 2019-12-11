list1 = [1, 2, 3, 8]
list2 = [1, 2, 3, 7]

list3 = list(map(lambda a,b : a+b , list1, list2)) 
print (str(list3))
