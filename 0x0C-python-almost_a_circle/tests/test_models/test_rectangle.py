""" a unit test for base of the figures """


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangleClassInstantiation(unittest.TestCase):
    """ class definition for test Rectangle class"""

    def test_object_instantiation_withEmptyArgument(self):
        """ function to test the Rectangel classe when object created with empty argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            b1 = Rectangle()

    def test_object_instantiation_withOneArgument(self):
        """ function to test the base classe when object is created with one argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            b1 = Rectangle(1)

    def test_2_object_instantiation_withTwoArgument(self):
        """ function to test the base classe when 2 objects are created with argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 2)
        R2 = Rectangle(2, 10)
        self.assertEqual(R2.id, R1.id + 1)

    def test_3_object_instantiation_withTwoArgument(self):
        """ function to test the Rectangle classe when 2 objects are created with argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R7 = Rectangle(10, 2)
        R8 = Rectangle(2, 10)
        R9 = Rectangle(20, 10)
        self.assertEqual(R9.id, R7.id + 2)


    def test_2_object_instantiation_withNoneArgument(self):
        """ function to test the Rectangle classe when object created with None argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(None)

    def test_object_instantiation_withThreeArgument(self):
        """ function to test the rectangle class when object is created with three arguments 

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 4, 5)
        R2 = Rectangle(4, 3, 7)
        self.assertEqual(R2.id, R1.id + 1)

    def test_object_instantiation_withfourArgument(self):
        """ function to test the rectangle class when object is created with four arguments 

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 4, 5, 8)
        R2 = Rectangle(4, 3, 7, 9)
        self.assertEqual(R2.id, R1.id + 1)

    def test_object_instantiation_withfiveArgument(self):
        """ function to test the rectangle class when object is created with five arguments 

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 4, 5, 8, 3)
        R2 = Rectangle(4, 3, 7, 9, 8)
        self.assertEqual(R2.id, R1.id + 5)

    def test_object_instantiation_withMoreThanfiveArgument(self):
        """ function to test the rectangle class when object is created with more than five 

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(10, 4, 5, 8, 3, 9)

    def test_object_instantiation_withFirstStringArgument(self):
        """ function to test the base classe when object created with first string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle("hey", 3)

    def test_object_instantiation_withSecondStringArgument(self):
        """ function to test the base classe when object created with first string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(3, "holberton")

    def test_object_instantiation_withThirdStringArgument(self):
        """ function to test the base classe when object created with third string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(3, 3, "holberton")

    def test_object_instantiation_withFourthStringArgument(self):
        """ function to test the base classe when object created with fourth string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(3, 4, 6, "holberton")

    def test_object_instantiation_withFiveStringArgument(self):
        """ function to test the rectangle classe when object created with first string argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 5, 2, 3, "holberton")
        self.assertEqual("holberton", R1.id)

    def test_object_instantiation_withFirstFloatArgument(self):
        """ function to test the rectangle classe when object created with fist float argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4.6, 4)

    def test_object_instantiation_withSecondFloatArgument(self):
        """ function to test the rectangle classe when object created with second float argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, 4.6)

    def test_object_instantiation_withThirdFloatArgument(self):
        """ function to test the rectangle classe when object created with third float argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, 6, 4.6)

    def test_object_instantiation_withFourthFloatArgument(self):
        """ function to test the rectangle classe when object created with fourth float argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, 4, 7, 4.6)



    def test_object_instantiation_withFiveFloatArgument(self):
        """ function to test the rectangle classe when object created with five float argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(4, 3, 4, 5, 45.6)
        self.assertEqual(45.6, R1.id)



    def test_Rectangle_is_Base(self):
        """ function to check whether a rectangle is an instance of Base

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 4)
        self.assertIsInstance(R1, Base)

    def test_object_instantiation_WithFirstListArgument(self):
        """ function to test the rectangle clas when object created passing first list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle([1, 2], 6)

    def test_object_instantiation_WithSecondListArgument(self):
        """ function to test the rectangle clas when object created passing second list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(6, [1, 2])

    def test_object_instantiation_WithThirdListArgument(self):
        """ function to test the rectangle clas when object created passing second list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(6, 7, [1, 2])

    def test_object_instantiation_WithFourthListArgument(self):
        """ function to test the rectangle clas when object created passing second list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(6, 7, 4, [1, 2])


    def test_object_instantiation_WithFifthListArgument(self):
        """ function to test the rectangle clas when object created passing five's list argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(3, 6, 5, 6, [1, 4])
        self.assertEqual([1, 4], R1.id)


    def test_object_instantiation_WithFirstDictArgument(self):
        """ function to test the rectangle classe when object created passing the first dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle({'width: 5'}, 2, 4, 5, 8)

    def test_object_instantiation_WithSecondDictArgument(self):
        """ function to test the rectangle classe when object created passing the second dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(5, {'height: 3'}, 4, 5, 8)

    def test_object_instantiation_WithThirdDictArgument(self):
        """ function to test the rectangle classe when object created passing the second dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(5, 6, {'height: 3'}, 4, 5)

    def test_object_instantiation_WithFourthDictArgument(self):
        """ function to test the rectangle classe when object created passing the second dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(5, 8, 3, {'height: 3'}, 4)

    def test_object_instantiation_WithFiveDictArgument(self):
        """ function to test the rectangle classe when object created passing the fifth dictionary argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 5, 4, 5, {'id': 5})
        self.assertEqual({'id': 5}, R1.id)


    def test_object_instantiation_WithFirstTupleArgument(self):
        """ function to test the base classe when object created passing first tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle((1, 2), 3, 4, 8, 5)

    def test_object_instantiation_WithSecondTupleArgument(self):
        """ function to test the base classe when object created passing second tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, (1, 2), 3, 4, 8)

    def test_object_instantiation_WithThirdTupleArgument(self):
        """ function to test the base classe when object created passing third tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, 5, (1, 2), 3, 4)

    def test_object_instantiation_WithForthTupleArgument(self):
        """ function to test the base classe when object created passing fourth tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(4, 4, 3, (1, 2), 3)

    def test_object_instantiation_WithFifthTupleArgument(self):
        """ function to test the rectangle class when object created passing fifth tuple argument
        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(3, 4, 6, 8, (1, 2))
        self.assertEqual(R1.id, (1, 2))

    def test_object_access_width_WithPrivateAttribute(self):
         """ function to test the base classe when object created using private attribute

         Arguments:
             nothing
         Returns:
             nothing
         """
         R1 = Rectangle(10, 5)
         with self.assertRaises(AttributeError):
             print(R1.__width)

    def test_object_access_height_PrivateAttribute(self):
         """ function to test when private value is accessed

         Arguments:
             nothing
         Returns:
             nothing
         """
         R1 = Rectangle(10, 5)
         with self.assertRaises(AttributeError):
             print(R1.__height)

    def test_object_access_x_PrivateAttribute(self):
         """ function to test when private value is accessed

         Arguments:
             nothing
         Returns:
             nothing
         """
         R1 = Rectangle(10, 5)
         with self.assertRaises(AttributeError):
             print(R1.__x)

    def test_object_access_y_PrivateAttribute(self):
         """ function to test when private value is accessed

         Arguments:
             nothing
         Returns:
             nothing
         """
         R1 = Rectangle(10, 5)
         with self.assertRaises(AttributeError):
             print(R1.__y)


""" test class for area """
class Test_Area_rectangle(unittest.TestCase):
    """ test class for area implementation """
    def test_area_with_no_argument(self):
        """ function to find area with no argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 5)
        self.assertEqual(50, R1.area())
    def test_area_with__argument(self):
        """ function to tese area with argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            R1.area(5)

    def test_area_with_larg_dimension(self):
        """ function to find area wiht large width

        Arguments:
            nothing
        Returns:
            nothing
        """
        r2 = Rectangle(2222222222222222222222222222222, 1033333333333333333333333)
        self.assertEqual(2296296296296296296296295555555325925925925925925925926, r2.area())

    def test_area_with_update_attribute(self):
        """ function to test area once the attribute has changed

        Arguments:
            nothing
        Returns:
            nothing
        """
        r3 = Rectangle(8, 7, 0, 0, 12)
        r3.width = 10
        self.assertEqual(r3.area(), 70)


""" test class test for display """
class Test_display(unittest.TestCase):
    """ display method implementation """
    
    def test_display_withargument(self):
        """ function to test display with argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(4, 6)
        with self.assertRaises(TypeError):
            R1.display(6)

    def test_display_withNoArgument(self):
        """ function to test display with no argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(2, 2)
        with patch('sys.stdout', new = StringIO()) as capture:
            R1.display()
            self.assertEqual(capture.getvalue(),"##\n##\n")

    def test_display_withNoArgument_differentDimenstion(self):
        """ function to test a display with various dimenstion

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(3, 4)
        with patch('sys.stdout', new = StringIO()) as capture:
            R1.display()
            self.assertEqual(capture.getvalue(),"###\n###\n###\n###\n")

    def test_display_with_x(self):
        """ function to test a display with various dimenstion

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(2, 2, 2)
        with patch('sys.stdout', new = StringIO()) as capture:
            R1.display()
            self.assertEqual(capture.getvalue(),"  ##\n  ##\n")

    def test_display_with_x_y(self):
        """ function to test a display with various dimenstion

        Arguments:
            nothing
        Returns:
            nothing
        """
        R1 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new = StringIO()) as capture:
            R1.display()
            self.assertEqual(capture.getvalue(),"\n\n  ##\n  ##\n")


""" test class for print """


class Test_print(unittest.TestCase):
    """ test cases to test the print function of the rectangle """

    def test_print_with_no_argument(self):
        """ function to test the print funciton without argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 6)
        self.assertEqual(print(), None)

    def test_print_with_one_argument(self):
        """ function to test the print funciton with one argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 6)
        with self.assertRaises(TypeError):
            r1.__str__(1)


    def test_print_with_argument_width_height(self):
       """ function to test the print function when only width & height provided

       Arguments:
           nothing
       Returns:
           nothing
       """
       r1 = Rectangle(10, 6)
       with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] ({}) 0/0 - 10/6\n".format(r1.id)
            self.assertEqual(capture.getvalue(),expected)

    def test_print_with_argument_width_height_x(self):
       """ function to test the print function when only width, height, x provide
d

       Arguments:
           nothing
       Returns:
           nothing
       """
       r1 = Rectangle(10, 6, 3)
       with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] ({}) 3/0 - 10/6\n".format(r1.id)
            self.assertEqual(capture.getvalue(),expected)

    def test_print_with_argument_width_height_x_y(self):
       """ function to test the print function when width, height, x, y provided

       Arguments:
           nothing
       Returns:
           nothing
       """
       r1 = Rectangle(10, 6, 3, 7)
       with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] ({}) 3/7 - 10/6\n".format(r1.id)
            self.assertEqual(capture.getvalue(),expected)

    def test_print_with_argument_width_height_x_y_id(self):
       """ function to test the print function when width, height, x, y & id provided

       Arguments:
           nothing
       Returns:
           nothing
       """
       r1 = Rectangle(10, 6, 3, 7, 12)
       with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (12) 3/7 - 10/6\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_print_with_argument_update_somevalue(self):
       """ function to test the print function when some value updated

       Arguments:
           nothing
       Returns:
           nothing
       """
       r1 = Rectangle(10, 6)
       r1.x = 9
       r1.y = 8
       with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] ({}) 9/8 - 10/6\n".format(r1.id)
            self.assertEqual(capture.getvalue(),expected)


""" test class for update method """

class Test_update(unittest.TestCase):
    """ class to test the update method of the rectangle class """
    
    def test_update_withNoArgument(self):
        """ function to test update without argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update()
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] ({}) 0/0 - 10/10\n".format(r1.id)
            self.assertEqual(capture.getvalue(),expected)


    def test_update_with_id_Argument(self):
        """ function to test update with id argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(89)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 10/10\n"
            self.assertEqual(capture.getvalue(),expected)
    
    def test_update_with_width_Argument(self):
        """ function to test update with id and width

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(89, 2)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 2/10\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_height_Argument(self):
        """ function to test update with id, width and height

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(89, 2, 2)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_x_Argument(self):
        """ function to test update with id, width, heigth and x

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(89, 2, 2, 5)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 5/0 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_y_Argument(self):
        """ function to test update with id, width, height, x & y

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(89, 2, 2, 3, 4)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 3/4 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)

      


    def test_update_with_id_keyword_Argument(self):
        """ function to test update with id argument

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 10/10\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_width_Keyword_Argument(self):
        """ function to test update with id and width

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89, width=2)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 2/10\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_height_Keyword_Argument(self):
        """ function to test update with id, width and height

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89, width=2, height=2)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 0/0 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_x_keyword_Argument(self):
        """ function to test update with id, width, heigth and x

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89, width=2, height=2, x=5)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 5/0 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)

    def test_update_with_y_keyword_Argument(self):
        """ function to test update with id, width, height, x & y

        Arguments:
            nothing
        Returns:
            nothing
        """
        r1 = Rectangle(10, 10)
        r1.update(id=89, width=2, height=2, x=3, y=4)
        with patch('sys.stdout', new = StringIO()) as capture:
            print(r1)
            expected = "[Rectangle] (89) 3/4 - 2/2\n"
            self.assertEqual(capture.getvalue(),expected)


if __name__ == '__main__':
    unittest.main()
