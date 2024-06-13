a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("The maximum number is:", max_num)