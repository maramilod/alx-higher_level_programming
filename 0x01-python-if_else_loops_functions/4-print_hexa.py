#!/usr/bin/python3
r = ""
for i in range(99):
    r += str(int(i)) + " = " + str(hex(i))
    if i != 98:
        r += "\n"
print(f"{r:s}")
