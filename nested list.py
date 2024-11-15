# Input Parsing
n = int(input())  # Number of students
students = []

for _ in range(n):
    name = input()  # Student's name
    grade = float(input())  # Student's grade
    students.append([name, grade])  # Add to the students list

# Finding Second Lowest Grade
grades = [student[1] for student in students]  # Extract grades from the students list
unique_grades = sorted(set(grades))  # Remove duplicates and sort grades
second_lowest_grade = unique_grades[1]  # Get the second lowest grade

# Finding Students with the Second Lowest Grade
names = [student[0] for student in students if student[1] == second_lowest_grade]  # Filter students by grade
sorted_names = sorted(names)  # Sort names alphabetically

# Printing Result
for name in sorted_names:
    print(name)
