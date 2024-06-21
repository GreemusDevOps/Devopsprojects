def generate_fibonacci(n):
    """
    Generate the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

# Test the function
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci(num_terms)
    print("Fibonacci sequence up to", num_terms, "terms:")
    print(fibonacci_sequence)
