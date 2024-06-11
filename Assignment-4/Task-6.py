#To check prime or not
N=int(input("Enter the number:"))
if N>1:
    for i in range(2,N):
        if(N%i)==0:
            print("The number you entered is not a Prime number",N)
            break
        else:
            print("The number you entered is a Prime number",N)