numbers = [1, 2, 3, 4, 5]
# Print the original list
print("Original list of numbers:", numbers)
# Add a new number to the list
new_number = 6
numbers.append(new_number)
# Print the list after adding a new number
print("List after adding", new_number, ":", numbers)
# Remove an existing number from the list
number_to_remove = 3
if number_to_remove in numbers:
    numbers.remove(number_to_remove)
    print("List after removing", number_to_remove, ":", numbers)
else:
    print(number_to_remove, "is not in the list.")

