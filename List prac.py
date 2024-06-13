fruits = ["apple", "banana", "orange", "kiwi"]
for i in fruits:
 print(i)
fruits[3]="grape"
print(fruits)
fruits.append("cherry")
print(fruits)
fruits.pop(2)
print(fruits)
if 'kiwi' in fruits:
   print("kiwi is there")
new=list(reversed(fruits))
print("After reversing:",new)
sorted_list=sorted(fruits)
print("list in Ascending order:",sorted_list)


list1=[1,20,3,4]
new=list(reversed(list1))
print("updated list after reversing:",new)

