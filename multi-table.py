def multi_table(no):
    if no <= 0:
        print("Please enter a positive integer.")
    else:
        for i in range(1,11):
            print(f"{no}", "X", i, "=", no*i)

no= int(input("Enter a number to print its multiplication table: "))
multi_table(no)