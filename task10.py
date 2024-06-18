def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)

    return list(intersection)
list1 = [10, 20, 30, 40, 50]
list2 = [40, 50, 60, 70, 80]
print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", find_intersection(list1, list2))
