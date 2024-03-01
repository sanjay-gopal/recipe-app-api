"""
Sample Test Cases
"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """ Tes the calc module"""

    def test_add_numbers(self):
        """Test Adding two numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 5+6)

    def test_subract_numbers(self):
        res = calc.subract(10, 15)
        self.assertEqual(res, 10-15)