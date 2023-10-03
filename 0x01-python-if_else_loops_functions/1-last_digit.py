#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
lastd = number[-1]
number = int(number)
lastd = int(lastd)
if number < 0:
    lastd *= -1
if lastd > 5:
    print(f"Last digit of {number:d} is {lastd:d} and is greater than 5")
if lastd == 0:
    print(f"Last digit of {number:d} is {lastd:d} and is 0")
if lastd < 6:
    print(f"Last digit of {number:d} is {lastd:d} and is less than 6 and not 0")
