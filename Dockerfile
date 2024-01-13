FROM python:3.9-slim

#Set the working directory
WORKDIR /app

#python scripts
COPY main.py .
COPY user.py .
COPY student.py .
COPY employee.py .
COPY applicant.py .

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker build -t UserType-app
# docker run UserType-app 