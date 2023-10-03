#!/usr/bin/python3
c = ""
for i in range(97, 123):
    if i != 113 and i != 101:
        c += chr(i)
print("{}".format(str(c)), end="")
