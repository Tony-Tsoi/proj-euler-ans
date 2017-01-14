"""
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

numStr = ''  # we are skipping the '0.' to avoid confusion

# for making 1-mil digits of the numStr, we need count to max around 199999 (hand-calculated)
for num in range(1, 199999):
    numStr += str(num)

product = 1

for i in range(7):
    index = 10 ** i - 1   # computers count from 0, but our index counts from 1
    product *= int(numStr[index])

print(product)