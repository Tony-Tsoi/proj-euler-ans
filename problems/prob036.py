"""
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from Euler import isDoubleBasePalindrome

total = 0

for k in range(1000000):
    if isDoubleBasePalindrome(k):
        total += k
        
print(total)