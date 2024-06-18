def count_word_occurrences(input_string):
    words = input_string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
input_string = "the quick brown fox jumps over the lazy dog"
print("Input string:", input_string)
print("Occurrences of each word:")
word_occurrences = count_word_occurrences(input_string)
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
