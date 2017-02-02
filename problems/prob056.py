"""
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
from Euler import sumOfDigits

maxSum = 1


for a in range(2, 100):
    for b in range(2, 100):
        if a % 10 is 0:
            a += 1
        cNum = a**b
        cSum = sumOfDigits(cNum)
        if cSum > maxSum:
            maxSum = cSum

print(maxSum)