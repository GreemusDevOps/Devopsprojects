def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Example usage:
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]
longest = find_longest_word(word_list)
print("The longest word is:", longest)
