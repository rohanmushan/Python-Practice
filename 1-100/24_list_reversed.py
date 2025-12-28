#Reverse a list in place.
numbers=[5,10,15,20,25]
numbers.reverse()
print(f"Reversed Numbers: {numbers}")

def list_reversed(num):
    """Reverses the List in place"""
    num.reverse()
    print(f"Reversed Numbers: {num}")
num = list(map(int, input("Enter numbers separated by space: ").split()))
list_reversed(num)