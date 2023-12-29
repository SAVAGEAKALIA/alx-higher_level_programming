#!/usr/bin/python3
"""Test case file for Rectangle """
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_area(self):
        """Tests the area method."""
        area_result = self.square.area()
        expected_area = 25
        self.assertEqual(area_result, expected_area)

    def test_display(self):
        """Tests the display method."""
        # Redirect stdout to capture printed output
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.square.display()
        displayed_output = sys.stdout.getvalue()
        expected_output = "\n" \
                          "\n" \
                          "\n" \
                          "  #####\n" \
                          "  #####\n" \
                          "  #####\n" \
                          "  #####\n" \
                          "  #####\n"
        self.assertEqual(displayed_output, expected_output)

        # Restore stdout
        sys.stdout = original_stdout

    def test_str_representation(self):
        """Tests the __str__ method."""
        str_result = str(self.square)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str_result, expected_str)

    def test_size_property(self):
        """Tests the size property and setter."""
        self.assertEqual(self.square.size, 5)

        self.square.size = 7
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.height, 7)

    def test_update_with_args(self):
        """Tests the update method with *args."""
        self.square.update(8, 9, 10, 11)
        self.assertEqual(self.square.id, 8)
        self.assertEqual(self.square.x, 10)
        self.assertEqual(self.square.size, 9)
        self.assertEqual(self.square.y, 11)

    def test_update_with_kwargs(self):
        """Tests the update method with **kwargs."""
        self.square.update(id=12, size=13, x=14, y=15)
        self.assertEqual(self.square.id, 12)
        self.assertEqual(self.square.size, 13)
        self.assertEqual(self.square.x, 14)
        self.assertEqual(self.square.y, 15)

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""
        dict_result = self.square.to_dictionary()
        expected_dict = {'id': 1, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(dict_result, expected_dict)


if __name__ == '__main__':
    unittest.main()
