"""
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# brute force
def applyRule(x):
    """
    x: an int
    output: an int after applying the rule
    """
    if x % 2 is 0:  # x is even
        return int(x/2)
    return int(3*x+1)
    
def getChainLen(x):
    """
    x: an int
    output: the length of chain
    """
    counter = 0
    while x is not 1:
        x = applyRule(x)
        counter += 1
    return counter
    
max_x = 1
max_l = 1
for i in range(1, 10**6):
    l = getChainLen(i)
    if l > max_l:
        max_l = l
        max_x = i

print(max_x)