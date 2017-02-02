"""
Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

* for the number see below *

"""
f = open('data\p013.txt')

num = 0
for line in f:
    num += int(line)

print (str(num)[:10])