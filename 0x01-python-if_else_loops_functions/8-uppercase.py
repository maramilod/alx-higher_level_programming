#!/usr/bin/python3
def uppercase(str):
    chaa = ""
    intt = 0
    d = len(str)
    for i in range(d):
        intt = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            intt -= 32
        chaa += chr(intt)
    print("{0:s}".format(chaa))
