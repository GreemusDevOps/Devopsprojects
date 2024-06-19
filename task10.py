
list_of_tuples = [(1,3),(1,2) ,(2, 3), (3,5), (4, 1), (5, 6)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print("Sorted list of tuples based on the second element:")
print(sorted_list)
