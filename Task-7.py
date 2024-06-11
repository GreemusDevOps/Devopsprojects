# To find the factorial of a number
def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
Num=int(input("Enter the number: "))
Factorial=fact(Num)
print("The factorial of a number is:",Factorial)

