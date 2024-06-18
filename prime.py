A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print (original_list)
def add_element(lst, element):
    lst.append(element)
def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    else:
        print(f"Element {element} not found in the list.")

