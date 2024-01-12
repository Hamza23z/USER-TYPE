from user import User
from student import Student
from employee import Employee
from applicant import Applicant

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