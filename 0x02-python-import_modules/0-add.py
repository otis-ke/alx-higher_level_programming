#!/usr/bin/env python3
"""
This module imports the add function from add_0.py
and prints the result of adding 1 and 2
"""

from add_0 import add

a = 1
b = 2

result = add(a, b)

print("{} + {} = {}".format(a, b, result))

