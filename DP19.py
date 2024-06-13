def longest_consecutive_sequence(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)
    return max_length
num_list = [8, 4, 5, 1, 3, 2]
print("Length of longest consecutive sequence:", longest_consecutive_sequence(num_list))
