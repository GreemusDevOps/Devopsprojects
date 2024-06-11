# Fibonacci Sequence
N=int(input("Enter the Number"))
def fib(N):
    if N==0 or N==1:
        return N
    elif N<0:
        return -1
    else:
        return fib(N-1)+fib(N-2)
fibonaci=fib(N)
print("The Fibonacci sequence is:",fibonaci)