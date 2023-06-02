#!/usr/bin/python3
import sys
args = sys.argv[1:]
result = sum(int(arg) for arg in args)
print(result)
