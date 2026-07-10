import csv

students = []


with open ("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


def get_home(student):
    return student["home"]

for student in sorted(students, key=lambda student:student ["name"]):
    print(f"{student['name']} is in {student['home']}")