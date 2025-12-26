#Calculate the area of a rectangle given its length and width
import random

length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")


#with function

def area_rect(l, w):
    """Returns the area of a rectangle given length and width and also generates random test cases"""
    return l * w
    print(f"Area of rect is {result}")
l = float(input("Enter Length of Rectangle: "))
w = float(input("Enter Width of Rectangle: "))
area_rect(l, w)


test_cases = 20
print("Random Test Case Results:\n")

for tc in range(1, test_cases + 1):
    test_length = random.uniform(1, 20)  
    test_width = random.uniform(1, 20)  
    test_area = area_rect(test_length, test_width)
    print(f"TC-{tc:02d} | Length: {test_length:.2f} | Width: {test_width:.2f} | Area: {test_area:.2f}")