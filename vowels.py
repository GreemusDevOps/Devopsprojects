def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    input_string = input_string.lower()
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
input_str = "Hello, Nageswari!"
print(f"The number of vowels in '{input_str}' is: {count_vowels(input_str)}")