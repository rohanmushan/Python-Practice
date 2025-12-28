#Merge two dictionaries into one.
dict1={'Akash':85,'Mahendra':92,'Rohan':78}
dict2={'Atipra':95,'Ram':88}
dict3={**dict1, **dict2}
print("Merged Dictionary: ")
print(merged_dict)

#with function
def dict_merge(d1, d2):
    """Merges two dictionaries into one"""
    merged_dict = {**d1, **d2}
    print("Merged Dictionary: ")
    print(merged_dict)

dict1 = {}
dict2 = {}
n1 = int(input("Enter number of entries for first dictionary: "))    
for i in range(n1):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    dict1[name] = score

n2 = int(input("Enter number of entries for second dictionary: "))    
for i in range(n2):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    dict2[name] = score

dict_merge(dict1, dict2)