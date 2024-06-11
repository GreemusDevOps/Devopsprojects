# checking common letters
string1=input('enter the first string:')
string2=input('enter the second string:')
y=list(set(string1)&set(string2))
print("The common letters are:")
for i in y:
    print(i)
