set1={'manu',28,"manu@Greemus.com"}
set2={'reddy',22,"reddy@Greemus.com"}
set1.update(set2)
print(set1)

set1={11,21,31,14}
set2={14,50,60,17}
intersection_set=set1&set2
print("intersection_set:",intersection_set)

set1={11,21,31,14}
set2={25,14,50,60,17}
union_set=set1|set2
print("union_set:",union_set)

Greemus_Dic={'Name':'Devi','ID':45,'Email':"abc@Greemus.com",'ID':45}
print (Greemus_Dic)

Greemus_Dic['Name']='Durga'
print (Greemus_Dic)

Greemus_Dic['Designation']='DevOps Engineer'
print (Greemus_Dic)

Greemus_Dic={'Name':'Devi','ID':45,'Email':"abc@Greemus.com",'ID':45}
print("Original dict:",Greemus_Dic)
Greemus_Dic.clear()
print("Original dict:",Greemus_Dic)

string = "rama is a goodboy"
vowels = "aeiou"
count = sum(string.count(vowel) for vowel in vowels)
print(count)

list=[2,8,25,10,23,15,14,12,13,33,30,40,60,50]
for i in list:
    if i %2 == 0:
        if index < len(i) - 1:
            print(i, end=',')
        else:
            print(i, end='')


dict = {1: 'manu', 2: 'boy',3: {'A': 'going', 'B': 'To', 'C': 'school'}}
print(dict)


