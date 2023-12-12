# ------------------------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# Rkhan, 12/11/2023,Created Script
# ------------------------------------------------------------------------------------------------- #


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