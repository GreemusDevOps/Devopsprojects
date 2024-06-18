def count_character_occurrences(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_str = "Hello, nageswari"
char_count = count_character_occurrences(input_str)
print(f"Character occurrences in '{input_str}':\n{char_count}")