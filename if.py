score=float(input('enter the students score'))
if score>90:
    grade='a'
elif score>75:
    grade='b'
elif score>65:
    grade='c'
else:
    grade='d'
print("the students grade is:",grade)

number=int(input("enter a number: "))
if number % 2 ==0:
    print(number,"is even.")
else:
    print(number,"is odd.")