def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    return input_string == input_string[::-1]
input_str = input("Enter a string")
if is_palindrome(input_str):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
