"""
Problem 8

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

* for the long 1000 digit number see below *

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

def containsZero(n):
    """
    n: an int or a str
    output: True if n contains '0'
    """
    numStr = str(n)
    for letter in numStr:
        if letter is '0':
            return True
    return False

f = open('data/p008.txt')
num = f.read()

maxProduct = 1

for i in range(len(num) - 13):
    substr = num[i : i+13]
    if not containsZero(substr):  # otherwise product == 0
        product = 1
        for digit in substr:
            product *= int(digit)
        if product > maxProduct:
            maxProduct = product
        
print (maxProduct)