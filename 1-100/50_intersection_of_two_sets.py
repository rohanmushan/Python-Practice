#Find the intersection of two sets
a={1, 2, 3, 4, 5, 6, 7} 
b={5, 6, 7, 8, 9, 10}
z=a.intersection(b)
print(z) 

#with function
def intersection_set(set1, set2):
    return set1.intersection(set2)
set1={1, 2, 3, 4, 5, 6, 7}
set2={5, 6, 7, 8, 9, 10}
intersection_set(set1, set2)