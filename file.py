fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt","r")
if fp:
    print("file is read success")



fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt","r")
if fp:
    print("file is read success")
content=fp.read()
print(content)

fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt","w")
fp.write("hello sita")
print(fp)

fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt","a")
fp.write("ram")
fp.close()


fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt",'r')
if fp:
    print("file is read success")

fp=open("C:\\Users\\LENOVO V330\\Desktop\\ram.txt",'w')
fp.write('ram')
fp.close()
fp=open("C:\\Users\\LENOVO V330\\Desktop\\manu.txt",'a')
fp.write('sita')
fp.close()

fp=open("C:\\Users\\LENOVO V330\\Desktop\\manu.txt",'r+')
fp.write('anji')
fp.close()






name="manu"
if 'gest' not in name:
    print("gest is not present in the name")
else:
    print("gest is in present in the name")





list=[1,2,3,4,5,6]
list1=[2,5,7,8,9]
set=set(list)
set1=set(list1)
result=set.intersection(set1)
print(result)