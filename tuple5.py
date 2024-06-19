tuple1=()
print("empty tuple:")
print(tuple1)
tuple2=(1,2,3,4,5,6)
print(tuple2)
list=[1,2,3,4,5,6]
print(tuple(list))
tuple3=("say hello","to","world")
print(tuple3)
tuple4=tuple("say hello")
print(tuple4)
tuple5=(9,8,7,6,5)
tuple6=("say hello","to","world")
tuple7=(tuple5,tuple6)
print(tuple7)
tuple8=("say hello",) * 3
print(tuple8)
tuple9=("say hello")
n=5
for i in range(int(n)):
    tuple9=(tuple9,)
    print(tuple9)
tuple10=("say hello to world")
print(tuple10[2])
print(tuple10[-1])
print(tuple10[::-1])
tuple11=("the", "lion", "is" ,"the"," king")
a,b,c,d,e=tuple11
print(a)
print(b)
print(c)
print(d)
print(e)
tuple12=(10,20,30,40)
tuple13=("elephant","lion","tiger")
tuple14=tuple12+tuple13
print(tuple14)
list1=['dog','rat','cow','rat','dog','cat','cat']
print(list1.count('dog'))
tuple15="thelion"
print(len(tuple15))
max_value=max(tuple12)
print(max_value)
tuple16=(100,200,600,300,500,400)
print(sorted(tuple16))
print(sorted(tuple16,reverse=True))
list3=[100,200,600,300,500,400]
print(sorted(list3))
list4=[100,200,600,300,500,400]
print(tuple(list4))
Tuple16 = ("A", 1, "B", 2, "C", 3)


print("Size of Tuple16: " ,tuple16.__sizeof__(), "bytes")
print("Size of Tuple14: " ,tuple14.__sizeof__(), "bytes")
print("Size of Tuple11: " ,tuple11.__sizeof__(), "bytes")