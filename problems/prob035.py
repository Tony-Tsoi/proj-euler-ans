"""
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from Euler import nextPrime, isPrime, contains

def circulate(n):
    """
    n: an int or a str of int
    output: a set of "circulations" of n, including n itself
    note: for definition of circulations, see question
    """
    numSet = set()
    numStr = str(n)
    numLen = len(numStr)
    if numLen is 1:
        numSet.add(n)
        return numSet
    
    for i in range(numLen):
        numStr = numStr[1:] + numStr[0]
        numSet.add(int(numStr))
    return numSet

def isPrimeList(L):
    """
    L: a list of int
    output: True if all int in L are primes
    """
    for num in L:
        if not isPrime(num):
            return False
    return True

def answer():
    cPrime = 2
    S = set()
    
    while cPrime < 10**6:  # less than a mil
        if cPrime is 2 or cPrime is 5:
            S.add(cPrime)
        elif not contains(cPrime, [2, 5, 0]) and cPrime not in S:
            L = circulate(cPrime)
            if isPrimeList(L):
                for elem in L:
                    S.add(elem)
        cPrime = nextPrime(cPrime)
    print(len(S))
    
    
if __name__ == "__main__":
    import time
    startTime = time.perf_counter()
    answer()
    endTime = time.perf_counter() - startTime
    print('Time elapsed', endTime)

