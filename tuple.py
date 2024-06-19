person=('Sasi',45,"hyderabad")
print (person)

person= "kumar"
print (person)


print(person[0:2])

print(person[:4])

person1=[10,20,30,40,50,60]
print("Tuple1:",person1)
dup_Tuple=[]
for i in person1:
    if i not in dup_Tuple:
        dup_Tuple.append(i)
print("Duplicate List:", dup_Tuple)