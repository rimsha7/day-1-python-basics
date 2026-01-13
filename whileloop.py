students = [
    {"name": "Umer", "gpa": 3.4},
    {"name": "Sidra", "gpa": 2.9},
    {"name": "Nida", "gpa": 3.8},
]
index = 0
while index<len(students):
    if students[index]["gpa"]>3.0:
        print(students[index]["name"])
    index += 1