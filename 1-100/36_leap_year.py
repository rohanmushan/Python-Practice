#Check if a year is a leap year.
year=int(input("Enter year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")

#with function
def is_leap_year(year):
    """Checks if a given year is a leap year. 
    when year is divisible by 4 but not by 100, or it is divisible by 400."""
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
year = int(input("Enter year: "))
is_leap_year(year)