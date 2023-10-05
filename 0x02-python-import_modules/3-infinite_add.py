#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lenght = len(sys.argv)
    if lenght != 1:
        for i in range(1, lenght):
            sum += int(sys.argv[i])
    print(sum)
