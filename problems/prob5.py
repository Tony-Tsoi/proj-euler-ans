"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def isDivRange(x, n):
    """
    x is the int to be tested
    n is the range to test from 2 inclusive to n inclusive
    """
    for i in range(n, 1, -1):
        if x % i is not 0:
            return False
    return True

cNum = 2520

while not isDivRange(cNum, 20):
    cNum += 20
    
print (cNum)