number=int(input("enter a number: "))
if number % 2 ==0:
    print('number is even')
else:
    print('number is odd')


number=int(input('enter the number: '))
if number % 2 == 1:
    print('number is odd')
else:
    print('number is even')

for i in range(10):
    if i == 5:
        continue
    print(i)


number=[11,22,33,44,55,66]
newnumber=77
number.append(newnumber)
print("after adding",newnumber,":" ,number)
number.remove(33)
print("afterremoving",number)

number=int(input('enter a value'))
if number%2==0:
    print('even number')
else:
    print('odd number')

for i in range(1,11):
    if i==5:
        break
        print(i)