# ------------------------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# Rkhan, 12/11/2023,Created Script
# ------------------------------------------------------------------------------------------------- #


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


