def sort_tuples_by_second_element(tuple_list):
    sorted_tuples = sorted(tuple_list, key=lambda x: x[1])
    return sorted_tuples
tuple_list = [(1, 6), (2, 3), (3, 8), (4, 1), (5, 2)]
print("Original list of tuples:", tuple_list)
sorted_tuples = sort_tuples_by_second_element(tuple_list)
print("Sorted list of tuples based on the second element:", sorted_tuples)