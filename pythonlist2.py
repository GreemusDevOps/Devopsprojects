List=[]
List.append(6)
List.append('manu')
List.append(4)
List.append('ram')
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
List.append((10,20))
print(List)
LIST2=['CHINNU','BUNNU']
List.append(LIST2)
print(List)

List.insert(-1,35)
List.insert(1,'mouni')
print(List)

list11=[10,20,30,20]
list11.extend([50,60,'manu'])
print(list11)
list11.reverse()
print(list11)
list11.__reversed__()
print(list11)
list11.remove(20)
list11.remove(50)
print(list11)

list12=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15]
for i in range(1, 5):
    list12.remove(i)
print(list12)
list12.pop()
list12.pop(6)
print(list12)

list13=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15]
print(list13[0:5])
print(list13[-1:])

print(list13[5:])
print(list13[:-1])
print(list13[::-1])

list14=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15]
list14.clear()
print(list14)

list15=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15]
print(list15.index(6))



