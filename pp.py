def swaplist(newlist):
    size=len(newlist)
    temp=newlist[1]
    newlist[1]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[12,34,55,25,30]
print(swaplist(newlist))


def swaplist(oldlist):
    size = len(oldlist)
    value=oldlist[3]
    oldlist[3]=oldlist[-2]
    oldlist[size-2]=value
    return oldlist
oldlist=[12,13,14,15,16]
print(swaplist(oldlist))


def findelement(list1,list2):
    return[list1[i] for i in list2]
list1=[10,20,30,40]
list2=[1,3]
print(findelement(list1, list2))

list11 = [1, 9, 8, 4, 9, 2, 9]
del list11[2][-3]
print(list11)