def remove_duplicates(input_list):
    unique_elements = set()
    result = []
    for item in input_list:
        if item not in unique_elements:
            result.append(item)
            unique_elements.add(item)

    return result
input_list = [1, 2, 3, 3, 2, 3, 5, 6, 2]
print("Original list:", input_list)
print("List after removing duplicates:", remove_duplicates(input_list))
