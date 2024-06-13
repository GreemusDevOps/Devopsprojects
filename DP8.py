def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci(terms))
