students = [
    {"name": "Umer", "gpa": 3.4},
    {"name": "Sidra", "gpa": 2.9},
    {"name": "Nida", "gpa": 3.8},
]
index = 0
while index<len(students):
    if students[index]["gpa"]>3.0:
        print(f"{students[index]["name"]} = {students[index]["gpa"]}")
    index += 1