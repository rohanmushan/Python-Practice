#Write a program to check if a number is prime.
no=int(input("Enter any number: "))
if(no>1):
    for i in range(2, no):
        if (no%i)==0:
            print(f"{no} is not a prime number")
            break
    else:
        print(f"{no} is a prime number")
else:
    print(f"{no} is not a prime number")

# with function
def prime(num):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                print(f"{num} is not a prime number")
                break
            else:
                print(f"{num} is a prime number")
                break
    else:
        print(f"{num} is not a prime number")

num = int(input("Enter a Number: "))
prime(num)

        
