#Print a pattern of numbers in an equilateral triangle.

rows=int(input("Enter rows for the triangle: "))
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#with function
def print_number_triangle(rows):
    """Prints an equilateral triangle pattern of numbers"""
    for i in range(1, rows+1):
        print(" " * (rows - i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

rows=int(input("Enter rows for the triangle: "))
print_number_triangle(rows)