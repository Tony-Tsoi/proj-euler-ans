"""
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from Euler import isPandigital, nextPrime

# Judging by the sum of pandigital numbers, only those with len() = 4 / 7 are not div by 3
def answer():
    lPrime = 1000
    cPrime = 1000000
    while cPrime < 10**7: # for num len = 7
        cPrime = nextPrime(cPrime)
        if isPandigital(cPrime):
            lPrime = cPrime
            
    if lPrime is 1000:  # in case there are no pandigital prime with len = 7
        while cPrime < 10**4:  # for num len = 4
            cPrime = nextPrime(cPrime)
            if isPandigital(cPrime):
                lPrime = cPrime
    
    print(lPrime)

if __name__ == "__main__":
    
    import time
    startTime = time.perf_counter()
    answer()
    endTime = time.perf_counter() - startTime
    print('Time elapsed', endTime)
