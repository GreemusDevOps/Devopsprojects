tuple_list = [(1,3),(4,2),(3,5),(6,1)]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print("sorted list:", sorted_list)