#!/usr/bin/python3
i = 122
c = ""
while i >= 97:
    j = i
    if i % 2 != 0:
        j -= 32
    c += chr(j)
    i -= 1
print("{:s}".format(c), end="")
