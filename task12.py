list=[2,3,5,7,11,13,17,19,23,29]
print("the original list=",list)
list.append(31)
print("after adding=",list)
list.remove(11)
print("after removing=",list)
exist_count = list.count(15)
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")