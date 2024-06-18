my_list = [10, 20, 30, 40]
print(my_list[2])
my_list.append(50)
print(my_list)
x=('hello')
x.capitalize()
print(x)


list=[10,20,30,40,50,10,40,50]
sum=sum(list)
print(sum)

list1=[1,2,3,5,6,7,2,5,3,4,8]
print('unique elements: ',(set(list1)))

set1={10,20,30,40,50,10,40,50,60,70,80,90,100}
set2={10,70,101,105,20,100}
union=set1|set2
print('unique_elements: ',union)

tuple1=(10,20,30,40,50)
tuple2=(10,20,30,40,60)
print('original tuple1: ',tuple1)
print('original tuple2: ',tuple2)
result=tuple1==tuple2
print('tuples are identical',result)

string='Ramaisagoodboy'
result = {x : string.count(x) for x in set(string) }
print('occurrences of each character: ',str(result))

string1='Ramaisagoodboy'
print(string1[::-1])

string3='Ramaisagoodboy'
reverses_string = string1[::-1]
print('given reverses_string: ',reverses_string)

list11=[10,2,30,40,5,10,4,50]
list12=[1,2,3,5,6,7,2,5,3,4,8]
set11=set(list11)
set12=set(list12)
result=set11.intersection(set12)
print('common elements between two lists: ',result)

x = "babu"
y = ""
for i in x:
    y = i + y

if (x == y):
    print('if it is a palindrome: ','Yes')
else:
    print('if it is a palindrome: ','No')

x = "mam"
y = ""
for i in x:
    y = i + y

if (x == y):
    print('if it is a palindrome: ','Yes')
else:
    print('if it is a palindrome: ','No')

string11='rama is a goodboy'
print('original string is: ',string11)
result=string11.capitalize()
print('string after capaitalize: ',result)

string12=('rama', 'is', 'a', 'goodboy')
for i in string12:
    output = i.capitalize()
    print(output, end=" ")






list22=['manu','ram','babu','chinnu','dev','haritha','varshini']
list22.sort()
print('sorts in alphabetical order: ',list22)

string88 = "rama is a goodboy"
vowels = "aeiou"
count = sum(string88.count(vowel) for vowel in vowels)
print(count)

