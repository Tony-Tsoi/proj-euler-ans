"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
# Brute-force method
from Euler import nextPrime

num = 10001  # the nth prime
cPrime = 0
for k in range(1, num + 1):  # from the 2nd prime to 10001st prime
    cPrime = nextPrime(cPrime)

print('finally', cPrime)