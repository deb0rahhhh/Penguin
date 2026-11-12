#!/usr/bin/env python3

import math
import sys

MULTIPLIER = 5

def square_and_multiply(num):
    return math.sqrt(num) * MULTIPLIER

user_val = input("Enter a positive numerical value: ")
try:
    user_val = float(user_val)
except:
    sys.exit("The input is not a number")
if (user_val < 0):
    sys.exit("Negative numbers are not allowed")
res = square_and_multiply(user_val)
print("The result after taking the square root of the number and multiplying it is:", res)
