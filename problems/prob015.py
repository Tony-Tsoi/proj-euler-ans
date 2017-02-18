"""
Problem 15
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""
from Euler import nCr

def answer():
    gSize = 20  # grid size
    print(nCr(gSize*2, gSize))

if __name__ == "__main__":
    answer()