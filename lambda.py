list_of_tuples = [(2, 10), (2, 5), (3, 8), (4, 2), (5, 6)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print("Sorted list of tuples based on the second element:")
print(sorted_list)