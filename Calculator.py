#Implement a simple calculator program that can perform addition, subtraction, multiplication, and division.

print("Simple Calculator")
print("Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Enter the number of your choice (1/2/3/4): "))

if option >4:
    print("Invalid choice")
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == 1:
        result = num1 + num2
        print("Result: ", result)
    elif option == 2:
        result = num1 - num2
        print("Result: ", result)
    elif option == 3:
        result = num1 * num2
        print("Result: ", result)
    elif option == 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result: ", result)
