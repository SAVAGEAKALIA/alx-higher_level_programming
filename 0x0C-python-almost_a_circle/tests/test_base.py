#!/usr/bin/python3
"""Test case file for base """
import unittest
from models.base import Base


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
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_default_id_assignment(self):
        """Tests that unique IDs are assigned when no ID is provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_provided_id_assignment(self):
        """Tests that the provided ID is assigned correctly."""
        b3 = Base(id=42)
        self.assertEqual(b3.id, 42)

    def test_object_count_maintained(self):
        """Tests that the object count is tracked accurately."""
        print(f"Initial object count: {Base.get_object_count()}")
        b1 = Base()
        print(f"After creating b1: {Base.get_object_count()}")
        b2 = Base(id=10)
        print(f"After creating b2: {Base.get_object_count()}")
        b3 = Base()
        print(f"After creating b3: {Base.get_object_count()}")
        self.assertEqual(Base._Base__nb_objects, 4)

    def test_to_json_string_with_list(self):
        """Tests to_json_string with a list of dictionaries."""
        dict_list = [{'id': 1, 'x': 2, 'y': 3}, {'id': 4, 'x': 5, 'y': 6}]
        json_str = Base.to_json_string(dict_list)
        expected_str = '[{"id": 1, "x": 2, "y": 3}, {"id": 4, "x": 5, "y": 6}]'
        self.assertEqual(json_str, expected_str)

    def test_to_json_string_with_empty_list(self):
        """Tests to_json_string with an empty list."""
        dict_list = []
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[]')

    def test_to_json_string_with_none(self):
        """Tests to_json_string with None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

    def test_from_json_string_with_valid_string(self):
        """Tests from_json_string with a valid JSON string."""
        json_str = '[{"id": 1, "x": 2, "y": 3}, {"id": 4, "x": 5, "y": 6}]'
        dict_list = Base.from_json_string(json_str)
        expected_list = [{'id': 1, 'x': 2, 'y': 3}, {'id': 4, 'x': 5, 'y': 6}]
        self.assertEqual(dict_list, expected_list)

    def test_from_json_string_with_empty_string(self):
        """Tests from_json_string with an empty string."""
        json_str = ''
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [])

    def test_from_json_string_with_none(self):
        """Tests from_json_string with None."""
        dict_list = Base.from_json_string(None)
        self.assertEqual(dict_list, [])


if __name__ == '__main__':
    unittest.main()
