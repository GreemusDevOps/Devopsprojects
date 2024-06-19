def count_word_occurrences(text):
    # Convert the text to lowercase to ensure case-insensitivity
    text = text.lower()

    # Remove punctuation marks
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in punctuation_marks:
        text = text.replace(char, " ")

    # Split the text into words
    words = text.split()

    # Initialize an empty dictionary to store word counts
    word_count = {}

    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Example usage:
input_text = "This is a sample text. This text contains some words, and some words may repeat."
word_occurrences = count_word_occurrences(input_text)
print("Word occurrences:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")