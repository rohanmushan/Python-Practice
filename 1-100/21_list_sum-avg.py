#Create a list of numbers and find the sum and average
numbers=[5,10,15,20,25]
add=sum(numbers)
ave=add/len(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {add}")
print(f"Average: {ave}")

#with function
def list_sum_avg(num):
    """Returns the sum and average of numbers in the List"""
    total=sum(num)
    average=total/len(num)
    print(f"Numbers: {num}")
    print(f"Sum: {total}")
    print(f"Average: {average}")

num = list(map(int, input("Enter numbers separated by space: ").split())) 
list_sum_avg(num)