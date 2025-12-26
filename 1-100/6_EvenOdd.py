# # Check if a number is even or odd.
import random

# number=int(input("Enter a number: "))
# if (number%2==0):
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

#with function
def even_odd(num):
    """Checks whether a number is even or odd and also generates random test cases"""
    if num % 2 == 0:
        print(f"The {num} is Even")
    else:
        print(f"The {num} is Odd")

num = int(input("Enter a Number: "))
even_odd(num)


NUM_TEST_CASES = 21
print("Random Test Case Results:\n")

for tc in range(1, NUM_TEST_CASES):
    test_input = random.randint(-20, 200)  
    print(f"TC-{tc:02d} | Input: {test_input:4} | Result: {'Even' if test_input % 2 == 0 else 'Odd'}")