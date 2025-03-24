class Student:
    """
    Basic class representing a student with a first name, last name, and GPA.
    """
    
    def __init__(self, first_name: str, last_name: str, gpa: float):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
    
    def student_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def student_honors(self):
        if self.gpa >= 3.5:
            return "Dean's List"
        elif self.gpa >= 3.25:
            return "Honor Roll"
        else:
            return None

    def evaluate_student(self):
        honors = self.student_honors()

        if honors is None:
            print(f"{self.student_name()} has made no honors")
        else:
            print(f"{self.student_name()} has made the {honors}")