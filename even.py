def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter_even_numbers(original_list)
print(even_list)