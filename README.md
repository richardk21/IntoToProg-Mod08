### Richard Khan
### 12/11/2023
###Foundation of Programming: Python
### Assignment07

#Creating Python Scripts

##Introduction
####Assignment 8 introduced us to unit testing and breaking out one's script.This assignment allowed us to categorize the data, presentation, and processing classes and test each one of them individually. This is important as our codes gets longer and more complicated, testing certain areas saves us in the end when testing the entire script. 

## Main.py

This script serves as the main entry point for the Employee Ratings program. It utilizes classes from various modules to manage employee data, input/output operations, and file processing.

```python
from data_classes import Employee, Person
from presentation_classes import IO
from processing_classes import FileProcessor

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''


# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,employee_data=employees,employee_type=Employee) 

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
```

##Data_classes.py

This module defines two classes, `Person` and `Employee`, representing person and employee data for the Employee Ratings program.

### `Person` Class

A class representing person data.

### Properties:

- `first_name` (str): The person's first name.
- `last_name` (str): The person's last name.

##### ChangeLog:

- Rkhan, 12.11.2023: Created the class.

```python
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}"
        
              
```

### `Employee` Class

A class representing employee data, inheriting from the `Person` class.

### Properties:

- `first_name` (str): The employee's first name.
- `last_name` (str): The employee's last name.
- `review_date` (date): The date of the employee review.
- `review_rating` (int): The review rating of the employee's performance (1-5).

##### ChangeLog:

- Rkhan, 12.11.2023: Created the class.

```python
import json
from datetime import date

class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

   ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating
        
    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")
          

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
```

These classes encapsulate person and employee data with specified properties, ensuring data integrity and providing string representations. The `Employee` class extends the `Person` class to reuse common properties. The classes include validation for certain property values and handle string conversions for better usability. 

##Test Data_class.py

```python
import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person = Person("Rich", "Khan")
        self.assertEqual(person.first_name, "Rich")
        self.assertEqual(person.last_name, "Khan")

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person("123", "Khan")
        with self.assertRaises(ValueError):
            person = Person("Rich", "123")

    def test_person_str(self):
        person = Person("Rich", "Khan")
        self.assertEqual(str(person), "Rich,Khan")

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee = Employee("Rich", "Khan","2023-01-05", 3)
        self.assertEqual(employee.review_date, "2023-01-05")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_date_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Rich", "Khan","invalid_review_date", 3)

    def test_employee_review_date_str(self):
        employee = Employee("2023-01-05")
        self.assertEqual(str(employee), "2023-01-05")

    def test_employee_review_rating_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Rich", "Khan", "2023-01-05","invalid_review_rating")

    def test_employee_review_rating_str(self):
        employee = Employee("3")
        self.assertEqual(str(employee), "3")

if __name__ == '__main__':
    unittest.main()
```

## Processing_classes.py

This module defines a class, `FileProcessor`, containing processing layer functions for working with JSON files in the Employee Ratings program.

### `FileProcessor` Class

A collection of processing layer functions that work with JSON files.
 
```python
import json
from data_classes import Employee, Person

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Methods:
    - read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list:
      Reads data from a JSON file and loads it into a list of dictionary rows.

    - write_employee_data_to_file(file_name: str, employee_data: list):
      Writes data to a JSON file with data from a list of dictionary rows.

    ChangeLog:
    - Rkhan, 12.11.2023: Created class.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list:
        """
        Reads data from a JSON file and loads it into a list of dictionary rows.

        Parameters:
        - file_name (str): Name of the file to read from.
        - employee_data (list): List of dictionary rows to be filled with file data.
        - employee_type (Employee): A reference to the Employee class.

        Returns:
        - list: Updated list of employee data.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name=employee["FirstName"]
                    employee_object.last_name=employee["LastName"]
                    employee_object.review_date=employee["ReviewDate"]
                    employee_object.review_rating=employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes data to a JSON file with data from a list of dictionary rows.

        Parameters:
        - file_name (str): Name of the file to write to.
        - employee_data (list): List of dictionary rows to be written to the file.

        Returns:
        - None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
```

##Test Processing_class.py
Here I tested the processing class to make sure I can write and read data to the Json files. 

```python

import unittest
import tempfile
import json
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name


    def tearDown(self):
        self.temp_file.close()

    def test_read_data_from_file(self):
        sample_data = [
            {"FirstName": "Bob", "LastName": "Baker", "ReviewDate": "2023-01-09", "ReviewRating": 4},
            {"FirstName": "Rich", "LastName": "Khan", "ReviewDate": "2023-01-05", "ReviewRating": 3}
        ]
        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data, file)

        Employees = FileProcessor.read_employee_data_from_file(sample_data, self.temp_file_name, "Employee")

        self.assertEqual(len(sample_data),len(Employees))

        self.assertEqual(Employees[0].FirstName, "Bob")
        self.assertEqual(Employees[0].LastName, "Baker")
        self.assertEqual(Employees[0].ReviewDate, "2023-01-09")
        self.assertEqual(Employees[0].ReviewRating, 4)


    def test_write_data_to_file(self):
        sample_data = [
            ("Jane", "Doe", "2023-04-10", 2)
                ]
        Employee = FileProcessor.write_employee_data_to_file(sample_data, self.temp_file_name)

        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(Employee))

        self.assertEqual(Employee[0].FirstName, "Jane")
        self.assertEqual(Employee[0].LastName, "Doe")
        self.assertEqual(Employee[0].ReviewDate, "2023-04-10")
        self.assertEqual(Employee[0].ReviewRating, 2)

    if __name__== '__main__':
        unittest.main()
```

This class provides methods to read and write employee data to and from JSON files. The `read_employee_data_from_file` function reads JSON data from a file and populates a list of employee data, and the `write_employee_data_to_file` function writes employee data to a JSON file. 

## Presentation_class.py

This module defines a class, `IO`, containing presentation layer functions that manage user input and output for the Employee Ratings program.

### `IO` Class

A collection of presentation layer functions that manage user input and output.

```python

class IO:
    """
    A collection of presentation layer functions that manage user input and output.

   ChangeLog:
    - Rkhan, 12.11.2023: Created class.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """
        Displays a custom error message to the user.

        Parameters:
        - message (str): String with message data to display.
        - error (Exception, optional): Exception object with technical message to display.

        Returns:
        - None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str) -> None:
        """
        Displays the menu of choices to the user.

        Returns:
        - None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice() -> str:
        """
        Gets a menu choice from the user.

        Returns:
        - str: String with the user's menu choice.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list) -> None:
        """
        Displays employee data to the user.

        Parameters:
        - employee_data (list): List of employee object data to be displayed.

        Returns:
        - None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()
    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """
        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data

```
##Test Presentation_Class.py

```python

import unittest
from unittest.mock import patch
from presentation_classes import IO
from presentation_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data =[]

    def test_get_input_menu_choice(self):
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_get_input_employee_data(self):
        with patch('builtins.input', side_effect=['Rich', 'Khan','2023-01-09', 3]):
            Employee =[]
            Employee = IO.input_employee_data(self.employee_data, employee_type=Employee)

            self.assertEqual(len(self.employee_data, len(Employee), 1)

            self.assertEqual(Employee[0]. FirstName,'Rich'),
            self.assertEqual(Employee[0].LastName, 'Khan'),
            self.assertEqual(Employee[0].EmployeeReviewData, '2023-01-09'),
            self.assertEqual(Employee[0].EmployeeReviewRating, 3)
            
if __name__=='__main__':
    unittest.main()
```

This class provides methods for displaying error messages, menus, and employee data to the user. The `input_menu_choice` function handles user input for menu choices, and the `output_employee_data` function displays employee data. 

###EmployeeRatings.json

```python
[{"FirstName": "Bob", "LastName": "Baker", "ReviewDate": "2023-01-09", "ReviewRating": 4},
  {"FirstName": "Rich", "LastName": "Khan", "ReviewDate": "2023-01-05", "ReviewRating": 3}
]
```
