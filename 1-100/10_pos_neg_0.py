#Write a program to check if a number is positive, negative, or zero.
no=int(input("Enter a Number: "))
if(no>0):
    print(f"{no} is Positive")
elif(no<0):
    print(f"{no} is negative")
else:
    print(f"{no} is Zero")

#with function
def pos_neg_zero(num):
    if num > 0:
        print(f"The {num} is Positive")
    elif num < 0:
        print(f"The {num} is Negative")
    else:
        print(f"The {num} is Zero")
num = int(input("Enter a Number: "))
pos_neg_zero(num)   