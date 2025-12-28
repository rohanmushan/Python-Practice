#Create a dictionary of student names and their scores, then find the average score
stud_scores={'Akash': 85,'Mahendra': 92,'Rohan': 78,'Atipra': 95,'Ram': 88}
avg_score=sum(stud_scores.values()) / len(stud_scores)
print("Student Scores: ")
for name, score in stud_scores.items():
    print(f"{name}: {score}")
print("\nAverage Score:", avg_score)

#with function
def dict_stud_avg(stud_scores):
    """Returns the average score of students in the dictionary"""
    avg_score=sum(stud_scores.values()) / len(stud_scores)
    print("Student Scores: ")
    for name, score in stud_scores.items():
        print(f"{name}: {score}")
    print("\nAverage Score:", avg_score)
stud_scores = {}
n = int(input("Enter number of students: "))    
for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    stud_scores[name] = score
dict_stud_avg(stud_scores)