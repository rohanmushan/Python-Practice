#Create a program that calculates the square root of a number.

import math

def sqrt_num(num):
    if num >= 0:
        square_root = math.sqrt(num)
        return f"The square root of {num} is {square_root}"
    else:
        return "Cannot calculate the square root of a negative number."
    
num = float(input("Enter a number: "))
print(sqrt_num(num))