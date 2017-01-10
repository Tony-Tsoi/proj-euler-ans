"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
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

number = 2000000
total = 0
cPrime = 0

# runs in O(n^2): don't do it
for j in range(1, number):
    cPrime = nextPrime(cPrime)
    if cPrime >= number:
        break
    total += cPrime
    
print("finally: " + str(total))