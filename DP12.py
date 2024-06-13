def count_word_occurrences(string):
    words = string.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

input_string = "apple banana apple orange banana kiwi"
print("Word occurrences:", count_word_occurrences(input_string))
