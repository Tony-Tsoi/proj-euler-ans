"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Brute-force method
import math

def isPrime(n):
  if (n == 2 or n == 3):
    return True
  if (n == 1 or n % 2 == 0 or n % 3 == 0):
    return False
  sqrtN = int(math.sqrt(n))
  for i in range(5, sqrtN, 6):
    if (n % i == 0 or n % (i+2) == 0):
      return False
  return True

def nextPrime(val):
  if isPrime(val):
    val += 1
  if (val % 2 == 0):
    val += 1
  while not isPrime(val):
    val += 2
  return val

number = 600851475143
cPrime = 1
lPrime = 1
counter = 1

while counter <= number:
  cPrime = nextPrime(cPrime)
  if number % cPrime == 0:
    lPrime = cPrime
    print("new lPrime:" + str(lPrime))
  if cPrime * cPrime >= number:
    break
    
print("finally: " + str(lPrime))