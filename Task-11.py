# finding the longest word in a list
def longestword(words):
    List= []
    for word in words:
        List.append((len(word),word))
    List.sort()
    print("The longest word is: ",List[-1][1])
a=["Apple","Banana","Mango","Strawberry","Berry","Guava"]
longestword(a)
