fruits = ["apple", "banana”, “Mango", "grape"]
# Use a for loop to iterate over the list of fruits and print each fruit
for fruit in fruits:
    print(fruit)
score = float(input("Enter the student's score: "))

if score > 90:
    grade = 'A'
elif score > 75:
    grade = 'B'
elif score > 65:
    grade = 'C'
else:
    grade = 'D'

print("The student's grade is:", grade)
