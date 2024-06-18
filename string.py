def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))
string1 = "Hello"
string2 = "Olelh"
print(are_anagrams(string1, string2))
string1 = "Python"
string2 = "Java"
print(are_anagrams(string1, string2))