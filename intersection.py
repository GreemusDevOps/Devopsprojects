def find_intersection(list1, list2):
    """
    Find the intersection of two lists.
    """
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", find_intersection(list1, list2))
