#Write a program that checks if a number is positive, negative, or zero.

def pos_neg(num):
    if(num > 0):
        print(f"{num} is a positive number")
    elif(num < 0):
        print(f"{num} is a negative number")
    elif(num == 0):
        print(f"{num} is zero")
    else:
        print("Invalid input")

number = float(input("Enter a number: "))
pos_neg(number)