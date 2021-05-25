""" a unit test for maxt integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class definition for the max_integer test"""
    def test_data_type(self):
        """ function to test the max_integer based on data type of the input

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Hey", 3, 456, "ALX", 65])

    def test_result(self):
        """ test max_integer giving variable input and check the output

        Arguments:
            nothing
        Returns:
            nothing
        """
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([-34, -2, -3, -37]), -2)
        self.assertEqual(max_integer([-231, 2, -33, -24]), 2)
        self.assertEqual(max_integer([23.4, 34.6, 56.5, 60.2]), 60.2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([56.3]), 56.3)
        self.assertEqual(max_integer([-34]), -34)
        self.assertEqual(max_integer(["holberton", "school","student"]), "student")

if __name__ == '__main__':
    unittest.main()
