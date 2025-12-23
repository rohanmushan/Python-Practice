#Create a program to convert temperature from Celsius to Fahrenheit and vice versa.

print("Temperature Conversion Program")
print("Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice")


#using function
def temp_conversion(celsius, fehrenheit):
    print("Choose the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choise = int(input("Enter your choice (1 or 2): "))
    if choise == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        Fahrenheit = (celsius *9/5) + 32
        print(f"{celsius} Celsius is Equal to {Fahrenheit} Fahrenheit")
    elif choise == 2:
        fehrenheit = float(input("Enter temperature in Fahrenheit: "))
        Celsius = (fehrenheit - 32) * 5/9
        print(f"{fehrenheit} Fahrenheit is Equal to {Celsius} Celsius")
    
    else:
        print("Invalid choice! Please select 1 or 2.")

