road=('bike','bus','car')
print(road)

print(road[0:1])
print(road[:4])
Tuple=[1,2,3,6,4,5,4,1]
print("Tuple1:",Tuple)
dup_Tuple2=[]
for i in Tuple:
    if i not in dup_Tuple2:
        dup_Tuple2.append(i)
print("Duplicate List:", dup_Tuple2)


tuple1=(10,20,30,40,50)
tuple2=[10,20,30,40,60]
print('original tuple1: ',tuple1)
print('original tuple2: ',tuple2)
result=tuple1==tuple1
print('tuples are identical',result)


string = "elephant rides a bike"
res = {x: string.count(x) for x in set(string)}
print("/n occurrence of all characters in elephant rides a bike is : " , str(res))

