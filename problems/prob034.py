"""
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

def isCurious(x):
    """
    x: an int to be checked
    output: True if is a curious number
    """
    numStr = str(x)
    total = 0
    for digit in numStr:
        total += math.factorial( int(digit) )
    return x == total

uBound = math.factorial(9)

t = 0

for num in range(3, uBound):  # exclude 1 and 2
    if isCurious(num):
        t += num
        print(num)

print('finally', t)