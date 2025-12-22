import math

def gmean(a, b):
    """calculate the geometric mean of a and b"""
    if a < 0 and b < 0:
        print("Geometric mean is not defined for negative numbers.")
    else:
        return math.sqrt(a * b)
    
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
result = gmean(a, b)
print(f"The geometric mean of {a} and {b} is {result}")