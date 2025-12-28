#Check if an element exists in a list
numbers=[5, 10, 15, 20, 25]
check=int(input("Enter num to check: "))
if(check in numbers):
    print(f"{check} exists in the list.")
else:
    print(f"{check} does not exist in the list.")

#with function
def list_exists(num, check):
    """Checks if an element exists in the List"""
    if(check in num):
        print(f"{check} exists in the list.")
    else:
        print(f"{check} does not exist in the list.")

num = list(map(int, input("Enter numbers separated by space: ").split()))
list_exists(num, check)
