#!/usr/bin/env python3
import sys

args = sys.argv[1:]
if len(args) == 0:
    print("0")
else:
    numbers = [int(arg) for arg in args]
    total = sum(numbers)
    print(total)
