#Calculate the product of two numbers entered by the user.

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
product=num1*num2
print(f"The product of {num1} and {num2} is: {product}")


#with function
"""Returns the product/Multiplication of two numbers"""
def product(num1, num2):
    prod = num1 * num2
    print(f"The product of {num1} and {num2} is {prod}")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
product(num1, num2)