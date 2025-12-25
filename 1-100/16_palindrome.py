#Write a program to check if a number is a palindrome.
num=int(input("Enter a number: "))
num=str(num)
reversed_str=num[::-1]
if (num==reversed_str):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#with function
def is_palindrome(number):
    num_str = str(number)
    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

number = int(input("Enter a number: "))
is_palindrome(number)