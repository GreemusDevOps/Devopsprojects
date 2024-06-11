# Intersection of two lists
def intersection(list1,list2):
    return list(set(list1) & set(list2))
list1=[1,2,3,4,3]
list2=[1,3,5,7,9]
print("List1 is:",list1)
print("List2 is:",list2)
intersection_list = intersection(list1,list2)
print("Intersection List is:",intersection_list)
