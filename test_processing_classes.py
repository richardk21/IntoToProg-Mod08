# ------------------------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# Rkhan, 12/11/2023,Created Script
# ------------------------------------------------------------------------------------------------- #

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