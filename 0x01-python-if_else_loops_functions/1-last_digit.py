#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number
sign = 0
if number < 0:
    lastd *= -1
    sign = 1
while lastd > 9:
    lastd %= 10
if sign == 1:
    lastd *= -1
if lastd > 5:
    print(f"Last digit of {number:d} is {lastd:d} and is greater than 5")
if lastd == 0:
    print(f"Last digit of {number:d} is {lastd:d} and is 0")
elif lastd < 6:
    print(f"Last digit of {number:d} is {lastd:d} and is less \
than 6 and not 0")
