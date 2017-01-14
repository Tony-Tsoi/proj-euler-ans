"""
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
def sumOfDiag(n):
    if n % 2 is 0 or n < 1:
        return
    
    if n is 1:
        return 1
      
    total = 1
    cNum = 1
    for cN in range(2, n, 2):
        for i in range(4):
            cNum += cN
            total += cNum
    
    return total

print(sumOfDiag(1001))