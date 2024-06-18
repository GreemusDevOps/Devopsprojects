def remove_duplicates(n):
    unique_list=list(set(n))
    return unique_list
org_list=[1,2,3,4,5,3,4,5]
unique=remove_duplicates(org_list)
print(unique)


