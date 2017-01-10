"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

# Brute-force method
import math

def isPrime(n):
    if (n == 2 or n == 3 or n == 5):
        return True
    if (n <= 1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
        return False
    sqrtN = int(math.sqrt(n)) + 1
    for i in range(5, sqrtN, 6):
        if (n % i == 0 or n % (i+2) == 0):
            return False
    return True

def nextPrime(val):
    if val < 2:
        return 2
    if isPrime(val):
        val += 1
    if (val % 2 == 0):
        val += 1
    while not isPrime(val):
        val += 2
    return val
  
num = 10001  # the nth prime
cPrime = 0
for k in range(1, num + 1):  # from the 2nd prime to 10001st prime
    cPrime = nextPrime(cPrime)
  
print('finally ' + str(cPrime))