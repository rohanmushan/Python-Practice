# Calculate the sum of two numbers entered by the user
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
sum=num1+num2
print(f"The sum of {num1} and {num2} is: {sum}")

# with function
def addition(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
addition(num1, num2)

