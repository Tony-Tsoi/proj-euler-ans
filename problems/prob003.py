"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Brute-force method
from Euler import nextPrime

number = 600851475143
cPrime = 1
lPrime = 1
counter = 1

while counter <= number:
    cPrime = nextPrime(cPrime)
    if number % cPrime == 0:
        lPrime = cPrime
    if cPrime * cPrime >= number:
        break
        
print('finally', lPrime)