#!/usr/bin/python3
print(*(f"{i} 0x{i:x}" for i in range(99)), sep='\n')
