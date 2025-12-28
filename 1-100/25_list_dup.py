#Write a program to remove duplicates from a list

numbers=[5,10,15,10,20,25,15,30]
dup_numbers=list(set(numbers))
print(f"Original List: {numbers}")
print(f"List without Duplicates: {dup_numbers}")

#with function
def duplicates(num):
    """Removes duplicates from the List"""
    unique_numbers = list(set(num))
    print(f"Original List: {num}")
    print(f"List without Duplicates: {unique_numbers}")
num = list(map(int, input("Enter numbers separated by space: ").split()))
duplicates(num)