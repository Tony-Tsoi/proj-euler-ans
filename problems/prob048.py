"""
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# brute-force method

num = 0

for i in range(1, 1001):
    num += i**i

print ( str(num)[-10:] )