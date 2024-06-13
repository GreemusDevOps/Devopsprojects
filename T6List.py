x1 = [1, 2, 3, 4, 5]
print("Original List:", x1)
new_number = int(input("number to add: "))
x1.append(new_number)
print("List after adding number:", x1)
remove_number = int(input("number to remove: "))
if remove_number in x1:
    x1.remove(remove_number)
    print("List after removing number:", x1)
else:
    print("Number not found in the list.")