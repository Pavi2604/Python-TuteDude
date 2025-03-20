student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Emma": 88
}

# Taking user input for student name
student_name = input("Enter the student's name: ")

# Retrieving and displaying the marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")