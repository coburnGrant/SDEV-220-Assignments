from Student import Student

test_students = [
    Student("John", "Smith", 4.0),
    Student("John", "Smith", 3.75),
    Student("John", "Smith", 3.5),
    Student("John", "Smith", 3.25),
    Student("John", "Smith", 3.0)
]

for student in test_students:
    student.evaluate_student()