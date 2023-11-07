#!/usr/bin/python3
"""
h
e
y
"""
save = __import__("5-save_to_json_file").save_to_json_file
lo = __import__("6-load_from_json_file").load_from_json_file
import sys


filen = "add_item.json"
parg = list(sys.argv[1:])

try:
    p = lo(filen)
except Exception:
    p = []

p.extend(parg)
save(p, filen)
