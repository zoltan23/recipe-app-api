"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        res = calc.add(4, 9)

        self.assertEqual(res, 13)

        res = calc.subtract(4, 0)
        
        self.assertEqual(res, 4)
