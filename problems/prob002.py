"""
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
total = 2
val1 = 1
val2 = 2
cVal = 3
while cVal <= 4000000:
    if cVal % 2 == 0:
        total += cVal
    val1 = val2
    val2 = cVal
    cVal = val1 + val2
print(total)