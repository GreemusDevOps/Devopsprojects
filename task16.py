def remove_last_element(input_list):
    if input_list:
        input_list.pop()
    else:
        print("The list is empty.")
my_list = [11, 12, 13, 14, 15]
print("Original list:", my_list)
remove_last_element(my_list)
print("List after removing the last element:", my_list)
