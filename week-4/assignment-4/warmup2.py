student = {
    "name": "Sarai",
    "grade": "A+",
    "subjects": ["Algebra", "Geology", "Microbiology"]
    }

#Print each key-value pair using .items() in a for loop

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False
print(student)