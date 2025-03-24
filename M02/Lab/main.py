# Name: Grant Coburn  
# File: main.py  
# Description: This script prompts the user to enter a student's first name, last name, and GPA.  
#              It then evaluates the student's academic honors.

from Student import Student

last_name = input("Enter student's last name: ")

if last_name == 'ZZZ':
    exit()

first_name = input("Enter student's first name: ")

gpa = float(input("Enter student's GPA: "))

Student(first_name, last_name, gpa).evaluate_student()
