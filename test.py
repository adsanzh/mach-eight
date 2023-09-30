import unittest
import os

from app import main

folder_path = './test_cases'
file_list = sorted([f for f in os.listdir(
    folder_path) if os.path.isfile(os.path.join(folder_path, f))])


class TestAssignment(unittest.TestCase):
    def test(self):
        for file in file_list:
            with open(f"./{folder_path}/{file}", 'r') as test_file:
                lines = test_file.readlines()
                expected_result = lines[-(len(lines) - 2):] if len(lines) > 2 else []
                expected_result = set(
                    tuple(map(int, item.strip().split(','))) for item in expected_result)

                result = main(lines[0], lines[1])

                sorted_result = set(tuple(sorted(inner_tuple))
                                    for inner_tuple in result)
                sorted_expected = set(tuple(sorted(inner_tuple))
                                      for inner_tuple in expected_result)

                self.assertEqual(sorted_result, sorted_expected)
