def is_prime(n):

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def first_n_primes(n):

    primes = []
    num = 2  # Start checking from 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


prime_numbers = first_n_primes(10)
print("List of the first 10 prime numbers:", prime_numbers)

def add_element(lst, element):

    if is_prime(element):
        lst.append(element)
        print("Element", element, "added successfully.")
    else:
        print("Error: Element is not a prime number.")

def remove_element(lst, element):

    if element in lst:
        lst.remove(element)
        print("Element", element, "removed successfully.")
    else:
        print("Error: Element not found in the list.")

def find_element(lst, element):

    if element in lst:
        print("Element", element, "found in the list at index", lst.index(element))
    else:
        print("Element", element, "not found in the list.")

add_element(prime_numbers, 31)
add_element(prime_numbers, 33)
remove_element(prime_numbers, 13)
remove_element(prime_numbers, 15)
find_element(prime_numbers, 7)
find_element(prime_numbers, 15)
