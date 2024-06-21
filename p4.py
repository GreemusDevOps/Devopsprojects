tl1=[(2,4),(10,8),(5,9)]
tl2=[(6,3),(2,7),(6,4)]
print("the original tl1=",tl1)
print("the original tl2=",tl2)
result=[(x[0]*y[0],x[1]*y[1])for x,y in zip(tl1,tl2)]
print(result)
tuple1=(3,4,5,6,7,8)
tuple2=(2,3,4,5,6,7)
print("the original =",tuple1)
print("the original =",tuple2)
res=tuple(ele1*ele2 for ele1,ele2 in zip(tuple1,tuple2))
print(res)