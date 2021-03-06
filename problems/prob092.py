"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
# brute force method
def sqDig(n):
    """
    n: an int or a str of int
    output: the square of the digits in n
    """
    retVal = 0
    
    aStr = str(n)
    for digit in aStr:
        retVal += int(digit) ** 2
    
    return retVal

counter = 0
for i in range(2, 10000000):
    cNum = i
    while True:
        cNum = sqDig(cNum)
        if cNum is 1:
            break
        if cNum is 89:
            counter += 1
            break

print(counter)