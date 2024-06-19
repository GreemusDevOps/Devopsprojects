def remove_duplicates(input_list):
    """
    Remove duplicates from a list.
    """
    return list(set(input_list))


input_list = [1, 2, 3, 4, 5, 2, 1, 5, 6, 5, 7]
print("Original list:", input_list)
print("List after removing duplicates:", remove_duplicates(input_list))
