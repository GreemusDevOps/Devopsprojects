#Removing duplicates from a list
List1=[1,2,3,4,3,5,6,7,1,2,5]
print("Original List is:",List1)
List2=[]
for i in List1:
    if i not in List2:
        List2.append(i)
print("The List after removal of duplicates is:",List2)