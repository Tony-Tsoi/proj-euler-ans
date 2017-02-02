"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from Euler import nextPrime

number = 2000000
total = 0
cPrime = 0

# runs in O(n^2): don't do it
for j in range(1, number):
    cPrime = nextPrime(cPrime)
    if cPrime >= number:
        break
    total += cPrime
    
print("finally", total)