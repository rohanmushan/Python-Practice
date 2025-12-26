#Write a program to find a maximum of three numbers.

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))

if(num1>num2) and (num1>num3):
   print(f"{num1} is greater")
elif(num2>num3) and (num2>num1):
   print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

#with function     
def max_of_three(num1, num2, num3):
   """Returns the maximum of three numbers and also generates random test cases"""
   if num1 > num2 and num1 > num3:
      return num1
   elif num2 > num3:
      return num2
   else:
      return num3
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
num3 = float(input("Enter a third number: "))

max_of_three(num1, num2, num3)

import random
test_cases = 20
print("Random Test Case Results:\n")

for tc in range(1, test_cases + 1):
   test_num1 = random.uniform(1.0, 1000.00)  
   test_num2 = random.uniform(1.0, 1000.00)
   test_num3 = random.uniform(1.0, 1000.00)  
   result = max_of_three(test_num1, test_num2, test_num3)
   print(f"TC-{tc:02d} | Num1: {test_num1:.2f} | Num2: {test_num2:.2f} | Num3: {test_num3:.2f} | Max is: {result:.2f}")