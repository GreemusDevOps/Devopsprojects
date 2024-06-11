# counting the occurrence of a word
def wordcount(string):
    my_dic = dict()
    words = string.split()
    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict
print(wordcount("Hai Durga My Name is also Durga"))
