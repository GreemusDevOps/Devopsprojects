def sort_tuples_by_second_element(tuple_list):
    # Sort the list of tuples based on the second element of each tuple
    sorted_tuples = sorted(tuple_list, key=lambda x: x[1])
    return sorted_tuples

# Example usage:
tuple_list = [(1, 5), (2, 3), (3, 8), (4, 1), (5, 7)]
sorted_tuples = sort_tuples_by_second_element(tuple_list)
print("Sorted list of tuples:", sorted_tuples)
