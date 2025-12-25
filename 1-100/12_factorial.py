# #Calculate the factorial of a number.

no=int(input("Enter a non-negative integer: "))
fact=1
if (no<0):
    print("Factorial is not defined for negative numbers.")
elif no==0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, no+1):
        fact=fact*i
    print(f"The factorial of {no} is {fact}")

#with function
def factorial(n):
    if n < 0:
        print("Factorial is not defined for the non zero numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact

n = int(input("Enter a non-negative integer: "))
print(factorial(n))