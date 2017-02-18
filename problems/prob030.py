"""
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def sumOfDigPow(n, a):  # sum of digits powered
    """
    n: an int
    a: the power of each digits
    output: sum of each digits of n with power of a
    """
    numStr = str(n)
    total = 0
    for digit in numStr:
        total += int(digit)**a
    return total

def answer():
    total = 0
    for num in range(2, 10**6):  # seems a reasonable upper bound
        if num == sumOfDigPow(num, 5):
            total += num
    print(total)
    
    
    
if __name__ == "__main__":
    import time
    startTime = time.perf_counter()
    answer()
    endTime = time.perf_counter() - startTime
    print('Time elapsed', endTime)
