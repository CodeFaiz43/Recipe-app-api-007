"""
Sample tests for calc module
"""

from django.test import SimpleTestCase

from app.calc import add,subtract


class CalcTests(SimpleTestCase):
    """Tests for calc module"""

    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers together"""
        res = subtract(10, 15)

        self.assertEqual(res, 5)
