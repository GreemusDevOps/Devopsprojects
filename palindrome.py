def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
input_str = "A man, a plan, a canal, Panama"
print(f"Is '{input_str}' a palindrome? {is_palindrome(input_str)}")
