class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        pass  

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print("Type: Student")

class Employee(User):
    def __init__(self, name, email, employee_id, department):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print("Type: Employee")

class Applicant(User):
    def __init__(self, name, email, application_id):
        super().__init__(name, email)
        self.application_id = application_id

    def display_info(self):
        print(f"Applicant Name: {self.name}")
        print(f"Application ID: {self.application_id}")
        print(f"Email: {self.email}")
        print("Type: Applicant")

# Creating User Instances
student = Student(name="Hamza", email="hamza001@gmail.con", student_id="2002")
employee = Employee(name="Noman", email="noman123@gmail.com", employee_id="E001", department="SE")
applicant = Applicant(name="Ali", email="ali101@gmail.com", application_id="A001")

# Displaying User Information
student.display_info()
print("\n")
employee.display_info()
print("\n")
applicant.display_info()
