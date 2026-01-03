#Check if a number is a perfect number
num=int(input("Enter number: "))
sum=0
for i in range(1, num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

#with function

def perfect_no(num):
    sum = 0
    for i in range(1, num):
        if(num %i == 0):
            sum = sum + i
            print(f"The {num} is a Perfect number")
        else:
            print(f"The {num} is not a Perfect number")

num = int(input("Enter number: "))
perfect_no(num)