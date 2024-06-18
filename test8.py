def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 6
print("number : ",num)
print("Factorial : ",factorial(num))