numbers = [1, 2, 3, 4, 5]
print("Original list of numbers:", numbers)
new_number = 6
numbers.append(new_number)
print("List after adding", new_number, ":", numbers)
number_to_remove = 3,5
if number_to_remove in numbers:
    numbers.remove(number_to_remove)
    print("List after removing", number_to_remove, ":", numbers)
else:
    print(number_to_remove, "is not in the list.")