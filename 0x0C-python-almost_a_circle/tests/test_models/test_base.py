""" a unit test for base of the figures """


import unittest
from models.base import Base


class TestBaseClassInstantiation(unittest.TestCase):
    """ class definition for test Base class"""

    def test_2_object_instantiation_withEmptyArgument(self):
        """ function to test the base classe when 2 object created

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3_object_instantiation_withEmptyArgument(self):
        """ function to test the base classe when 3 objects created

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_object_instantiation_withSomeArgument(self):
        """ function to test the base classe when object created with argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base(3)
        b2 = Base(5)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 5)

    def test_2_object_instantiation_withNoneArgument(self):
        """ function to test the base classe when object created

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_2_object_instantiation_withEmptyAndArgument(self):
        """ function to test the base classe when object is created using both empty and some argument 

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base()
        b2 = Base(5)
        self.assertEqual(b2.id, b1.id + 4)

    def test_object_instantiation_withStringArgument(self):
        """ function to test the base classe when object created with string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base("hey")
        self.assertEqual(b1.id, "hey")

    def test_object_instantiation_withFloatArgument(self):
        """ function to test the base classe when object created with float

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base(3.6)
        self.assertEqual(b1.id, 3.6)

    def test_object_instantiation_WithPublicAttribute(self):
        """ function to test the base classe when object created using public attribute

        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base()
        b1.id = 10
        self.assertEqual(b1.id, 10)

    def test_object_instantiation_WithListArgument(self):
        """ function to test the base classe when object created passing list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base([1, 2])
        self.assertEqual(b1.id, [1, 2])

    def test_object_instantiation_WithDictArgument(self):
        """ function to test the base classe when object created passing dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base({'id': 14})
        self.assertEqual(b1.id, {'id': 14})

    def test_object_instantiation_WithtupleArgument(self):
        """ function to test the base classe when object created passing tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_object_instantiation_WithtTwoArguments(self):
        """ function to test the base classe when object created passing two arguments
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_object_instantiation_WithPrivateAttribute(self):
         """ function to test the base classe when object created using private attribute

         Arguments:
             nothing
         Returns:
             nothing
         """
         b1 = Base()
         with self.assertRaises(AttributeError):
             print(b1.__nb_objects)


class TestToJsonConvertion(unittest.TestCase):
    """ class definition for test Base class to json conversion"""


    def test_to_json_withEmptyArgument(self):
        """ function to test to_json method with empty argument """
        
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_withOneArgument_not_dictionary(self):
        """ function to test to_json method with non dictionary argument """

        r1 = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            Base.to_json_string(r1)

    def test_to_json_withOneArgument_valid_dictionary(self):
        """ function to test to_json method with valid dictionary """

        r1 = Rectangle(5, 6)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string(dictionary)
        self.assertEqual(str, type(json_dict))

    def test_to_json_with_valid_argument_square(self):
        """ function to test to_json method with square type """

        s1 = Square(4, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string(s1.to_dictionary())

    def test_to_json_withMorthanOneArgument(self):
        """ function to test to_json method with more than one argument """

         r1 = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            Base.to_json_string(r1, 2)

    def test_to_json_with_list_of_rectangles(self):
        """ function to test to_json method with two rectangles """

        r1 = Rectangle(3, 4, 5, 6, 6)
        r2 = Rectangle(7, 8, 9, 9, 5)
        list_dict = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(str, type(Base.to_json_string(list_dict)))

    def test_to_json_with_list_of_square(self):
        """ function to test to_json method with two squares """

        s1 = Square(4, 5, 6, 7)
        s2 = Square(6, 7, 8, 9)
        list_dict = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(str, type(Base.to_json_string(list_dict)))

    def test_to_json_with_None_argument(self):
        """ function to test to_json method with None argument """

        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_with_empty_list(self):
        """ function to test to_json method with empty list """

        self.assertEqual("[]", Base.to_json_string([]))


        
if __name__ == '__main__':
    unittest.main()
