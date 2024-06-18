string = "rama is a goodboy"
vowels = "aeiou"
count = sum(string.count(vowel) for vowel in vowels)
print('count of vowels: ',count)

string1 = "cat"
string2 = "act"
if (string1,string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

list=[2,8,25,10,23,15,14,12,13,33,30,40,60,50]
for i in list:
    if i %2 == 0:
        print(i,end=',')

string1 = "rama is a goodboy"
print('original string is: ',string1)
result=string1.upper()
print('string after upper: ',result)




num_list=[10,20,30,40,50,200,34,500,400]
maxvalue=max(num_list)
minvalue=min(num_list)
print("Maximum value:", maxvalue)
print("Minimum value:", minvalue)
