def count_vowels(string):
    """
    Count the number of vowels in a given string.
    """
    vowels = "aeiouAEIOU"  # Define the set of vowels
    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Test the function
input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))
