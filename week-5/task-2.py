import json

# Read original JSON
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

# Calculate average grade
for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)

# Write to a new JSON file
with open("students1.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
