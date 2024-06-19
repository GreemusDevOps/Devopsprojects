list1 = [1, 2, 2,2,3, 3, 4, 4, 5,5,5,6,7,8]
list2= []
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)
