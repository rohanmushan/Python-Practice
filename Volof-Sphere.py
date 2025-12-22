#Create a program that calculates the volume of a sphere.
import math
def vol_of_sphere(r):
    volume = (4/3) * math.pi * (r ** 3)
    print(f"The volume of the sphere with radius {r} is {volume}")

radius = float(input("Enter the radius of the sphere: "))
vol_of_sphere(radius)