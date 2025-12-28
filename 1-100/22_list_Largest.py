#Find the largest and smallest elements in a list
numbers=[5, 10, 15, 20, 25]
largest=max(numbers)
smallest=min(numbers)
print(f"Numbers: {numbers}")
print(f"Largest Element: {largest}")
print(f"Smallest Element: {smallest}")

#with function
def list_largest_smallest(num):
    """Returns the largest and smallest elements in the List"""
    largest_element=max(num)
    smallest_element=min(num)
    print(f"Numbers: {num}")
    print(f"Largest Element: {largest_element}")
    print(f"Smallest Element: {smallest_element}")

num = list(map(int, input("Enter numbers separated by space: ").split()))
list_largest_smallest(num)