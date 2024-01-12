from user import User
from student import Student

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