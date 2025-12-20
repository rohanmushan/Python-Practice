#Implement a program that checks if a number is prime.
import random
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



NUM_TEST_CASES = 20

print("Random Test Case Results:\n")

for tc in range(1, NUM_TEST_CASES + 1):
    test_input = random.randint(-20, 200)  
    result = is_prime(test_input)

    print(f"TC-{tc:02d} | Input: {test_input:4} | Result: {'Prime' if result else 'Not Prime'}")