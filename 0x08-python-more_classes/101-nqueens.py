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
    li = []
    arr = []
    ar = []
    arra = []
    for i in range(n):
        x = i
        arr = []
        for j in range(n):
            if j != x and j != (n - d):
                ar = [x, j]
                arr.append(ar)
        arra.append(arr)
        d += 1

    array = [i for s in arra for i in s]
    i = 1

    for j in array:
        li.append(j)
        i += 1
        if i == n + 1:
            print(li)
            li = []
    print(li)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    cal(int(sys.argv[1]))
