from user import User
from student import Student
from employee import Employee

class Applicant(User):
    def __init__(self, name, email, application_id):
        super().__init__(name, email)
        self.application_id = application_id

    def display_info(self):
        print(f"Applicant Name: {self.name}")
        print(f"Application ID: {self.application_id}")
        print(f"Email: {self.email}")
        print("Type: Applicant")