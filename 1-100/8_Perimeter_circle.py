#Calculate the perimeter of a circle given its radius
radius=float(input("Enter the radius of the circle: "))
circumference=2*3.14*radius
print(f"The circumference of the circle is: {circumference}")

#with function

def perimeter_circle(r):
    """Returns the perimeter of a circle given its radius"""
    circumference = 2 * 3.14 * r 
    print(f"The perimeter of the circle with radius {r} is: {circumference}")

r = float(input("Enter Radius of Circle: "))
perimeter_circle(r)