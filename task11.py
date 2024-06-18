def find_longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
words = ["manu", "chinnu", "ravi", "sai", "manohar reddy"]
print("List of words:", words)
print("Longest word:", find_longest_word(words))
