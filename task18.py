def find_common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_characters = set1.intersection(set2)
    return common_characters
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common_chars = find_common_characters(string1, string2)
print("Common characters between the two strings:", common_chars)
