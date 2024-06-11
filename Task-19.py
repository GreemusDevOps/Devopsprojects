#longest word
input_sequence=input("Enter the sequence:")
y=max(input_sequence.split(), key=len)
print("Longest word is:",y)
print("Length of word is:",len(y))
