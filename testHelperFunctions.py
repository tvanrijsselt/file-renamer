"""Module to run unittests"""

import unittest
import helperFunctions

class TestHelperFunctions(unittest.TestCase):
    """This is a class docstring"""
    def test_path_ends_on_backslash(self):
        """This is a function docstring"""
        self.assertEqual(helper_functions.path_ends_on_backslash('my_path\\folder\\pictures'), \
                                                                'my_path\\folder\\pictures\\')
        self.assertEqual(helper_functions.path_ends_on_backslash('my_path\\folder\\videos\\'), \
                                                                'my_path\\folder\\videos\\')

if __name__ == '__main__':
    unittest.main()
