set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}
union_result = set1.union(set2)
intersection_result = set1.intersection(set2)
difference_set1_set2 = set1.difference(set2)
difference_set2_set1 = set2.difference(set1)
print("Union of the sets:", union_result)
print("Intersection of the sets:", intersection_result)
print("Difference of set1 - set2:", difference_set1_set2)
print("Difference of set2 - set1:", difference_set2_set1)