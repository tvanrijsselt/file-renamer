"""Module to run unittests"""

import unittest
import helper_functions


class TestHelperFunctions(unittest.TestCase):
    """This is a class docstring"""

    def test_path_ends_on_backslash(self):
        """This is a function docstring"""
        original_path = 'my_path\\folder\\videos'
        adjusted_path = 'my_path\\folder\\videos\\'
        self.assertEqual(helper_functions.path_ends_on_backslash(
            original_path), adjusted_path)


if __name__ == '__main__':
    unittest.main()
