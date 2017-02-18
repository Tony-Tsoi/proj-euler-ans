"""
Problem 18

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
(see file)

NOTE: As there are only 16384 routes, it is possible to solve this problem 
by trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""
def answer():
    f = open('data\p018.txt')
    L = []
    for line in f:
        L.append(list(map(int, line.split())))
    
    for i in range(len(L)-2, -1, -1):
        for j in range(len(L[i])):
            L[i][j] += max(L[i+1][j], L[i+1][j+1])
    print(L[0][0])

if __name__ == "__main__":
    import time
    startTime = time.perf_counter()
    answer()
    endTime = time.perf_counter() - startTime
    print('Time elapsed', endTime)