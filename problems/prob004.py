"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from Euler import isPalindrome
  
lPal = 0
  
# for 2 three-digit number, i and j
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if isPalindrome(product) and product > lPal:
            lPal = product

print('finally', lPal)