students = [
    {"name": "Umer", "gpa": 3.4},
    {"name": "Sidra", "gpa": 2.9},
    {"name": "Nida", "gpa": 3.8},
]

for student in students:
    if student["gpa"] > 3.0:
        print(student["name"])
