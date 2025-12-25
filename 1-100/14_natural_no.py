#Print the first N natural numbers using a for loop.
N=int(input("Enter value of N: "))
print(f"The first {N} natural numbers are:")
for i in range(1, N+1):
    print(i)
 
#with function
def natural_numbers(n):
    print(f"The first {n} natural numbers are:")
    for i in range(1, n+1):
        print(i)

N = int(input("Enter value of N: "))
natural_numbers(N)