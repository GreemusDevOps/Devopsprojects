list=[]
print("blank list:",list)
list1=[1,2,3,4,5,6]
print("list with numbers:",list1)
list2=[1,2,3,4,5,"hello"]
print("list with mixed:",list2)
list3=[1,2,5,6,7,8],["hello","world"]
print("list with mixed values:",list3)
list4=[1,2,2,3,4,5,6,6,6,7,8]
print("list with duplicat numbers:",list4)
list.append(1)
list.append(2)
list.append(3)
print("list after adding:",list)
list1.remove(3)
list1.remove(5)
print("list after removig:",list1)
print(list2[2])
print(list4[2])
print(list1[-2])
print(list4[-2])
print(list4[:-2])
print(list4[::-2])
print(list4[:-1])
print(list4[::-1])
string= "say hello to world"
list6= string.split()
print('The list is:', list6)