#Write a Python program that swaps the values of two variables without using third variable.

def swap(a, b):
    print("Before swapping: a =", a, "b =", b)
    a, b = b, a
    print("After swapping: a =", a, "b =", b)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
swap(a ,b)


#Write a Python program that swaps the values of two variables using third variable.
def swap(a, b):
    print("Before swapping: a =", a, "b =", b)
    temp = a
    a = b
    b = temp
    print("After swapping: a =", a, "b =", b)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
swap(a ,b)
