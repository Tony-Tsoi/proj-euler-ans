"""
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def isPalindrome(num):
    """
    num: an int or a str of int
    output: True if is palindromic
    """
    aString = str(num)
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

total = 0

for k in range(1000000):
    if isDoubleBasePalindrome(k):
        total += k
        
print(total)