n = int(input())  # Number of students
student_marks = {}

# Reading input for student names and their scores
for _ in range(n):
    name, *line = input().split()  # Name and scores
    scores = list(map(float, line))  # Convert scores to floats
    student_marks[name] = scores  # Store in dictionary

query_name = input()  # Name of the student to query

# Function to calculate average
def avg(scores):
    return sum(scores) / len(scores)

# Get the result for the queried student
result = avg(student_marks[query_name])

# Print the result formatted to 2 decimal places
print(f"{result:.2f}")
