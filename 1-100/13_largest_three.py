#.Find the largest among three numbers using nested if-else.

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))

if(num1>num2 and num1>num3):
       print(f"{num1} is greater")
elif(num2>num1 and num2>num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

#with function

def largest_of_three(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        print(f"{num1} is the largest")
    elif(num2 > num1 and num2 > num3):
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: ")) 
num3 = int(input("Enter num3: "))
largest_of_three(num1, num2, num3)