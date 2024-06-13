def count_vowels(string):
  vowels = 'aeiouAEIOU'
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count
string = input("Enter a string: ")
count = count_vowels(string)
print("The number of vowels in the string is:", count)