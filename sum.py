#Write a Python program that takes two numbers as input and prints their sum.

def sum(num1, num2):
    return num1 + num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    
print(f"Sum of {num1} and {num2} is {sum(num1, num2)}")
