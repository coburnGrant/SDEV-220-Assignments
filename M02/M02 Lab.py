
last_name = input("Enter student's last name: ")

if last_name == 'ZZZ':
    exit()

first_name = input("Enter student's first name: ")

gpa = input("Enter student's GPA: ")

gpa = float(gpa)

student_name = f"{first_name} {last_name}"

if gpa >= 3.5:
    print(f"{student_name} has made the Dean's List")
elif gpa >= 3.25:
    print(f"{student_name} has made the Honor Roll")
else:
    print(f"{student_name}'s GPA is {gpa}")
