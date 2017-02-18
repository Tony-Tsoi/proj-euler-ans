"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Euler import pFac
    
def answer():
    number = 600851475143
    print(pFac(number)[-1])
    
if __name__ == "__main__":
    import time
    startTime = time.perf_counter()
    answer()
    endTime = time.perf_counter() - startTime
    print('Time elapsed', endTime)