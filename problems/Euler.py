"""
These are the methods that are commonly used for solving 
my Project Euler questions.
"""
import math

def isPrime(n):
    """
    n: an int
    output: True if n is prime
    """
    if (n is 2 or n is 3):
        return True
    if (n <= 1 or n % 2 is 0 or n % 3 is 0):
        return False
    sqrtN = int(math.sqrt(n)) + 1
    for i in range(5, sqrtN, 6):
        if (n % i is 0 or n % (i+2) is 0):
            return False
    return True
    
def nextPrime(n):
    """
    n: an int
    output: the nearest prime > n
    """
    if n < 2:
        return 2
    if isPrime(n):
        n += 1
    if n % 2 is 0:
        n += 1
    while not isPrime(n):
        n += 2
    return n

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

def sumOfDigFac(n):
    """
    n: an int / str of int
    output: the sum of the factorials of the digits in n
    """
    numStr = str(n)
    total = 0
    for digit in numStr:
        total += math.factorial(int(digit))
    return total

def isPalindrome(n):
    """
    n: an str
    output: True if the str is a palindrome
    """
    aString = str(n)
    length = len(aString)
    for i in range(int(length / 2)):
        if aString[i] != aString[length - i - 1]:
            return False
    return True

def isDoubleBasePalindrome(x):
    """
    x: an int or a str of int
    output: True if is double base palindromic
    """
    numStr = str(x)
    if not isPalindrome(numStr):
        return False
    
    # change to base 2 and test again
    numStr = str(bin(x))[2:]
    return isPalindrome(numStr)

def isDivRange(x, L):
    """
    x: an int
    L: a list
    output: True if x is divisible by all the numbers in L
    """
    for i in L:
        if x % i is not 0:
            return False
    return True

def numFac(n):
    """
    n: an int
    output: num of factors n has
    """
    if n is 1:
        return 1
        
    c = 0  # counter
    for x in range(1, int(math.ceil(math.sqrt(n)))):
        if n % x is 0:
            c += 2
    return c

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

def nCr(n, r):
    """
    n: an int
    r: an int that is smaller than n (not checked)
    output: the value of nCr
    """
    return int( math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) ))

def isPandigital(n):
    """
    n: an int
    output: True if is a pandigital
    """
    if len(str(n)) > 10:
        return False
    
    numStrList = list(str(n))
    
    if len(str(n)) is 10:
        numList = list(range(10))
    else:
        numList = list(range(1, len(str(n))+1))
    
    for num in numList:
        if str(num) not in numStrList:
            return False
    return True


def contains(n, L):
    """
    n: an int or a str of int
    L: a list of int w/ len = 1
    output: True if n contains at least one elem in L
    """
    numStrList = list(str(n))
    for num in L:
        if num in numStrList:
            return True
    return False

def pFac(n):
    """
    n: an int
    output: a set of distinct prime factors
    """
    if n < 2 or isPrime(n):
        return []
    
    pSet = set()
    i = 2
    while i <= n:
        while n % i is 0:
            pSet.add(i)
            n = int(n / i)
        i = nextPrime(i)
    return pSet

if __name__ == "__main__":
    print('These are the methods that are commonly '
        + 'used for solving my Project Euler questions.')