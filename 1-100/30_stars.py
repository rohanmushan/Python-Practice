#Print a pattern of stars in the shape of a right-angled triangle.
rows=int(input("Enter the rows for the triangle: "))
for i in range(1, rows+1):
    print('*' * i)

#with function
def print_stars_triangle(rows):
    """Prints a right-angled triangle pattern of stars"""
    for i in range(1, rows+1):
        print('*' * i)