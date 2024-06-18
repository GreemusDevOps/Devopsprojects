def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    string = string.lower()
    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count
input_string = input("Enter a string: ")
print("Number of vowels in the given string:", count_vowels(input_string))
