"""
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
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

num = 2**1000
print (sumOfDigits(num))