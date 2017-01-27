"""
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from math import factorial

def sumOfDigits(n):
    """
    n: a number in int / str of int
    output: the sum of the digits in n
    """
    numStr = str(n)
    total = 0
    for digit in numStr:
        total += int(digit)
    return total
  
product = factorial(100)
print (sumOfDigits(product))