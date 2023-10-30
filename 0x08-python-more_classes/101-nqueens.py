#!/usr/bin/python3
import sys
"""
h
e
y
"""


def cal(n):
    """
    h
    """

    d = 1
    arr = []
    ar = []
    for i in range(n):
        x = i
        arr = []
        for j in range(n):
            if j != x and j != (n - d):
                ar = [x, j]
                arr.append(ar)
        print(arr)
        d += 1

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        cal(n)
    except IndexError:
        print("Please provide an integer as a command line argument.")
    except ValueError:
        print("The command line argument must be an integer.")
