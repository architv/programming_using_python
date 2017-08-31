"""
Given a positive integer n write a program which goes from 1 to n and:
print "Fizz" if the number is divisble by 3
print "Buzz" if the number is divisible by 5
print "FizzBuzz" if the number is divisible by both 3 and 5
"""

n = 100 # assuming n to be 100
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
