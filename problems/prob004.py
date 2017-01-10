"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
 # checks if the number is palindrome
def isPalindrome(num):
    aString = str(num)
    length = len(aString)
    for i in range(int(length / 2)):
        if aString[i] != aString[length - i - 1]:
            return False
    return True
  
lPal = 0
  
 # for 2 three-digit number, i and j
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if isPalindrome(product) and product > lPal:
            lPal = product
            print('newPal ' + str(lPal))

print(lPal)