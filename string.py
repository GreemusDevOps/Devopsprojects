def is_palindrome(input_string):
    processed_string = input_string.replace(" ", "").lower()
    return processed_string == processed_string[::-1]
test_string = "A man, a plan, a canal, Panama"
result = is_palindrome(test_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
