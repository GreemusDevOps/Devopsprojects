num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


print("the first natural numbers=")
for i in range(1,11):
    print(i)

n=6
num1 = 0
num2 = 1
next_number = num2
count = 1
print("Fibonacci sequence:", end=" ")
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

print("Tables:")
for i in range(1, 11):
    for j in range(1, 11):
        print(i, '*', j, '=', i * j)

squares = [x ** 2 for x in range(1, 11)]
print("List of squares of numbers from 1 to 10:")
print(squares)


keys = ["manu", "ram", "mouni"]
values = [2, 6, 7]
res = {}
for key in keys:
	for value in values:
		res[key] = value
		values.remove(value)
		break
print("Resultant dictionary is : ",res)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5:
        print("Encountered 5. Breaking the loop.")
        break
    if num == 3:
        print("Encountered 3. Skipping to the next iteration.")
        continue
    print("Current number:", num)
print("Loop finished.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("current number:" )
for num in numbers:
    if num == 5:
        print("Encountered 5. Breaking the loop.")
        break
    if num == 3:
        print("Encountered 3. Skipping to the next iteration.")
        continue
    print(num)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
print("number : ",num)
print("Factorial : ",factorial(num))


my_list = [(1, 3), (5, 2), (7, 8), (6, 4)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print("Sorted list based on the second element:")
print(sorted_list)

numerator = 70
denominator = 0
if denominator != 0:
	result = numerator / denominator
else:
	print("Error: Cannot divide by zero.")

def add_prime(prime_list, new_prime):
    prime_list.append(new_prime)

def remove_prime(prime_list, prime_to_remove):
    if prime_to_remove in prime_list:
        prime_list.remove(prime_to_remove)

def find_prime(prime_list, prime_to_find):
    if prime_to_find in prime_list:
        return True
    else:
        return False

prime_numbers = [2, 3, 5, 7, 11, 17, 19, 23, 29, 31]

print("Original list of prime numbers:", prime_numbers)

new_prime_number = 13
add_prime(prime_numbers, new_prime_number)
prime_to_remove = 5
remove_prime(prime_numbers, prime_to_remove)
print("Updated list of prime numbers after add and remove operations:", prime_numbers)
number_to_find = 17
if find_prime(prime_numbers, number_to_find):
    print(number_to_find, "is found in the list.")
else:
    print(number_to_find, "is not found in the list.")


tuple = ("apple", 10,1.00, "manu", [1, 2, 3])
for i in tuple:
 print(i)

 student_scores = {
     "reddy": 86,
     "manu": 77,
     "ram": 68,
     "manohar": 91,
     "mouni": 81
 }
 highest_score_student = max(student_scores, key=student_scores.get)
 highest_score = student_scores[highest_score_student]
 print("Student with the highest score name :", highest_score_student)
 print("Score:", highest_score)

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

stack = []
stack.append(10)
stack.append(15)
stack.append(20)
print('Initial stack')
print(stack)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)