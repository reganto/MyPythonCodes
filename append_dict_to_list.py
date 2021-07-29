# Author: Reganto
# Blog: reganto.net

students = []

for _ in range(3):
    name = input("Enter the new student name: ")
    school = input("Enter the new student school: ")

    student = {"name": name, "school": school}
    students.append(student)

print(students)
