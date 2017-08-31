"""
Given a positive integer n
Print all the prime numbers from 2 to n
"""

n = 100  # assuming n to be 100

for i in range(2, n+1):
    # flag to check if the number is divisble by a number other than 1 or itself
    flag = False
    # go from 2 to i-1 and check if it is divisible by any of them, if yes break and go to next iteration
    for n in range(2, i):
        if i % n == 0:
            flag = True
            break

    if not flag:
        print(str(i) + " is prime")


"""
This can be done using a more efficient way
Instead of going through all numbers and checking if its a prime
we just need go till the square root of that number to check if it is prime or not
"""

# we need math library for using the square root function
import math

for i in range(2, n+1):
    # flag to check if the number is divisble by a number other than 1 or itself
    flag = False
    # go from 2 till the sqrt of i and check if it is divisible by any of them, if yes break and go to next iteration
    for n in range(2, int(math.sqrt(i)) + 1):
        if i % n == 0:
            flag = True
            break

    if not flag:
        print(str(i) + " is prime")