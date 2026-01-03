Pi=3.14  
Radius=float(input("Enter radius of circle: "))  
area=Pi*Radius*Radius  
print("The area of circle is: ",area)

#with function 
def area_circle(Radius):
    Pi=3.14
    area=Pi*Radius*Radius
    print(f"The area of circle is {area}")
Radius=float(input("Enter radius of circle: "))
area_circle(Radius)