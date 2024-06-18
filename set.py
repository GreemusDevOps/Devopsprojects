greemus={'manu',108,'manu@greemus'}
print(greemus)
greemus.add(108)
print(greemus)
greemus.add(109)
print(greemus)
greemus.remove(108)
print(greemus)




num = int(input("Enter a number: "))
for i in range(2, int(number ** 0.5) + 1):
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")