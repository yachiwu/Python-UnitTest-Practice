import unittest
from src.Employee import Employee
from unittest.mock import patch , MagicMock

class TestEmployee(unittest.TestCase):
    @patch('src.Employee.requests.get')
    def test_monthly_schedule(self, mock_request_get):
        # arrange
        emp = Employee('John', 'Doe', 50000)
        mock_request_get.return_value = MagicMock(ok=True,text="Mock response text")

        # act
        schedule = emp.monthly_schedule('January')

        # assert
        self.assertEqual(schedule, 'Mock response text')

                    