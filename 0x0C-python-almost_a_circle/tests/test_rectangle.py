#!/usr/bin/python3
"""Test case file for Rectangle """
import unittest
from models.rectangle import Rectangle, Base
from io import StringIO
import sys


class TestBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method runs once before any tests in the class
        # cls.initial_count = Base.get_object_count()
        print(f"Initial object count: {Base.get_object_count()}")

    @classmethod
    def tearDownClass(cls):
        # This method runs once after all tests in the class
        print(f"Final object count: {Base.get_object_count()}")

    def setUp(self):
        self.rectangle = Rectangle(1, 2, 3, 4, 5)
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_default_Rectangle_function(self):
        """ Test that rectangle function works fine """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(20, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_provided_id_assignment_Rectangle(self):
        """Test Rectangle function with provided id"""
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r3.id, 12)

    def test_setter_and_getter_methods(self):
        """ Test case for Setter and Getter Methods"""
        r = Rectangle(10, 20)

        r.width = 15
        self.assertEqual(r.width, 15)

        r.height = 25
        self.assertEqual(r.height, 25)

        r.x = 5
        self.assertEqual(r.x, 5)

        r.y = 10
        self.assertEqual(r.y, 10)

    def test_invalid_width(self):
        """Test invalid width."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 20, 2, 3, 1)
        self.assertEqual(str(context.exception), "width must be > 0.")

    def test_invalid_height(self):
        """Test invalid height."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, -5, 2, 3, 1)
        self.assertEqual(str(context.exception), "height must be > 0.")

    def test_invalid_x(self):
        """Test invalid x."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, -2, 3, 1)
        self.assertEqual(str(context.exception), "x must be >= 0.")

    def test_invalid_y(self):
        """Test invalid y."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, 2, -3, 1)
        self.assertEqual(str(context.exception), "y must be >= 0.")

    def test_non_integer_width(self):
        """Test non-integer width."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle("10", 20, 2, 3, 1)
        self.assertEqual(str(context.exception), "width must be an integer.")

    def test_non_integer_height(self):
        """Test non-integer height."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "20", 2, 3, 1)
        self.assertEqual(str(context.exception), "height must be an integer.")

    def test_non_integer_x(self):
        """Test non-integer x."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 20, "2", 3, 1)
        self.assertEqual(str(context.exception), "x must be an integer.")

    def test_non_integer_y(self):
        """Test non-integer y."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 20, 2, "3", 1)
        self.assertEqual(str(context.exception), "y must be an integer.")

    def test_string_x(self):
        """ Test string. """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(20, 19, "help", 4, 1)
        self.assertEqual(str(context.exception), "x must be an integer.")

    def test_area(self):
        """Test area method."""
        r = Rectangle(5, 10, 0, 0, 1)
        self.assertEqual(r.area(), 50)
        self.assertEqual(r.id, 1)

    def test_display(self):
        """Test display method."""
        r = Rectangle(3, 2, 1, 1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '\n ###\n ###\n')

    def test_str_method(self):
        """ Test String method"""
        rect = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(rect), expected_output)

    def test_str(self):
        """Test str method."""
        r = Rectangle(5, 10, 2, 1, 1)
        expected_output = "[Rectangle] (1) 2/1 - 5/10"
        self.assertEqual(str(r), expected_output)


    def test_set_attributes(self):
        """Test setting attributes using setattr."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_update_with_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (1, 2, 3, 4, 5))

    def test_update_with_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, height=2, x=3, y=4, id=5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (5, 1, 2, 3, 4))

    def test_update_with_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(1, 2, width=3, height=4, x=5, y=6, id=7)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (1, 2, 10, 10, 10))

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""
        dict_result = self.rectangle.to_dictionary()
        expected_dict = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(dict_result, expected_dict)

if __name__ == '__main__':
    unittest.main()
