students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#Top scorer
top_score = -1
top_student = ""

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_student = student["name"]
print(f"{'Top scorer:':<18}{top_student} ({top_score})")

#Class average
total = 0
for student in students:
    total += student["score"]
average = total/len(students)
print(f"{'Class average:':<18}{average}")    

#Subjects offered
subjects = set()

for student in students:
    subjects.add(student["subject"])
print(f"{'Subjects offered:':<18}{subjects}")

#Highe scorers
high_scores = []

for student in students:
    if student["score"] > 75:
        high_scores.append(student["name"])
print(f"{'High scorers:':<18}{high_scores}")    
    



