def fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence
num_terms = int(input("Enter the number of terms in the Fibonacci sequence"))
sequence = fibonacci_sequence(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:")
print(sequence)

