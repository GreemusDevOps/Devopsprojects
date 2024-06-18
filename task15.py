def sum_of_elements(input_list):
    total_sum = 0
    for element in input_list:
        total_sum += element

    return total_sum
input_list = [1, 2, 3, 5, 8]
print("Input list:", input_list)
print("Sum of all elements:", sum_of_elements(input_list))
