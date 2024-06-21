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


numbers = [100, 4, 200, 1, 3, 2, 5, 101, 102, 103]
longest_sequence_length = longest_consecutive_sequence(numbers)
print("Length of the longest consecutive sequence:", longest_sequence_length)
