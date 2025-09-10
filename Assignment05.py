# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and \
# exception handling.
# Change Log: (Who, When, What)
# Aanya, 8/13/2025, Created Script
# -------------------------------------------------------------------------- #

import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
    Select from the following menu:
    1. Register a Student for a Course.
    2. Show current data. 
    3. Save data to a file.
    4. Exit the program. 
-------------------------------------
'''

FILE_NAME: str = "Enrollments.json"

# The constant values do not change throughout the program.

# Define the Data Variables and Constants
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
file = open(FILE_NAME, "r")


class Enrollments:
    pass


for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    students.append(student_data)
    file.close()

    # Present and Process the data
    while (True):

        # Present the menu of choices
        print(MENU)
        menu_choice = input("What would you like to do? ")

        # Input User Data
        if menu_choice == "1":
            try:
                student_first_name = input("Enter the student's first name: ").strip()
                if student_first_name == "":
                   raise ValueError("First name cannot be empty.")
                student_last_name = input("Enter the student's last name: ").strip()
                if student_last_name == "":
                    raise ValueError("Last name cannot be empty.")
                course_name = input("Enter the course's name: ").strip()
                if course_name == "":
                    raise ValueError("Course name cannot be empty.")

                student_data = {
                    "first_name": student_first_name,
                    "last_name": student_last_name,
                    "course_name": course_name,
                }
                students.append(student_data)
                print(f" You have registered {student_first_name} {student_last_name} for {course_name}.\n")

            except ValueError as ve:
                print("Input Error:", ve, "\n")
            continue

        # Present the Current Data
        elif menu_choice == "2":
            if len(students) == 0:
                print("No students registered yet.\n")
            else:
                print("-"*50)
            for student in students:
                print(f"{student[0]}: {student[1]} is enrolled in {student[2]}.")
            print("-"*50)
            continue

        # Save the Data to a File
        elif menu_choice == "3":
            try:
                file = open(FILE_NAME, "w")
                for student in students:
                    json.dump = (f"{student[0]},{student[1]},{student[2]}\n")
                    file.write(Enrollments.json)
                file.close()
                print("The following data was saved to file!")
                for student in students:
                    print(f"{student[0]}: {student[1]} is enrolled in {student[2]}.")
            except Exception as e:
                print("Error saving data:", e, "\n")
                continue



        # Stop the Loop
        elif menu_choice == "4":
            break  # out of the loop
    else:
            print("Please only choose option 1, 2, 3, 4")
    print("Program ended")
