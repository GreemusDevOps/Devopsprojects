def remove_last_element(input_list):
    if input_list:  # Check if the list is not empty
        input_list.pop()  # Remove the last element using the pop() method

# Example usage:
my_list = [1, 2, 3, 4, 5]
remove_last_element(my_list)
print("List after removing the last element:", my_list)
