def remove_last_element(lst):
    if lst:
        lst.pop()
    return lst

my_list = [1, 2, 3, 4, 5]
print("List after removing last element:", remove_last_element(my_list))
