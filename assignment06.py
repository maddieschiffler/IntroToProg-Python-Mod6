# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: Maddie, 11/17/24, downloaded assignment starter
#             Maddie, 11/18/24, made changes with classes and functions
#             Maddie, 11/19/24, finalized code while working with review video
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Variables and Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads student data from a file
        :param file_name: Name of the file we are reading student data from
        :param student_data: List of dictionary rows we are reading from
        :return: list
        """
        #global FILE_NAME

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.",error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name:str,student_data:list):
        """
        This function writes student data to a Json file
        :param file_name: Name of the file that student data is written to
        :param student_data: List of dictionary rows we are writing to
        """
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            print("\nThe following data was saved to file:")
            IO.output_current_data(student_data=student_data)
            # for student in students:
            #     print(f'Student {student["FirstName"]} '
            #           f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    A collection of presentation layer functions that manage user input and output
    """
    @staticmethod
    def output_error_messages(message:str, error: Exception = None):
        """
        This function displays the error messages to the user
        :param message: Message to display to indicate error
        :param error: Error that is displayed
        """
        print(message, end="\n\n")
        if error != None:
            print(" -- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of options to the user
        :param menu: String that includes the options menu
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function asks the user to select from the menu
        :param: None
        """
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Choose only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice


    @staticmethod
    def output_current_data(student_data:list): # might need to be output_student_courses
        """
        This function displays the current data to the user
        :param student_data: List of dictionary rows we are displaying
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        return student_data

    @staticmethod
    def input_student_data(student_data:list):
        """
        This function asks the user for student data
        :param student_data: List of dictionary rows we are adding data to
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Incorrect data type", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a problem with the data entered.", error=e)
        return student_data

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Main body: Present and Process the data
while (True):
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue
    # Present the current data
    elif menu_choice == "2":
        #student_table = IO.input_student_data(student_data=students)
        IO.output_current_data(student_data=students)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended. Goodbye")
