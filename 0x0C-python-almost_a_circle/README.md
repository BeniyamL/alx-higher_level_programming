# Python - Almost a circle

## Description

This project covers how to build basic block of big python project like AirBnB project.This includes concepts like Unit testing, serialization and deseralization of a python class, writing and reading JSON file, handling named arguments, arguments.
---
## Requirements
### Python Scripts

    * Allowed editors: vi, vim, emacs
    * All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    * All your files should end with a new line
    * The first line of all your files should be exactly #!/usr/bin/python3
    * A README.md file, at the root of the folder of the project, is mandatory
    * Your code should use the PEP 8 style (version 1.7.*)
    * All your files must be executable
    * The length of your files will be tested using wc
    * All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
    * All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    * All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

### Python Unit Tests

    * Allowed editors: vi, vim, emacs
    * All your files should end with a new line
    * All your test files should be inside a folder tests
    * You have to use the unittest module
    * All your test files should be python files (extension: .py)
    * All your test files and folders should start with test_
    * Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
    * All your tests should be executed by using this command: python3 -m unittest discover tests
    * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
   
---
 
## How the project works

    * first the project finds the main method
    * read each line of the main method and call the necessary function when it requies
    * execute the requrired function
---

## Usage

    * download the source code from the github repository
    * write the main method and call the required function from the downloaded file
    * execute the main method
---
## Tasks

   * 0. make All your files, classes and methods must be unit tested and be PEP 8 validated.

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: tests/

   * 1. Write the first class Base

   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py, models/__init__.py

   * 2.Write the class Rectangle that inherits from Base:
   
   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 3.Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 4. Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
    
    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 5.Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character 
    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 6. Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
    
    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 7. Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character  by taking care of x and y

   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 8. Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 9. Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

   Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 10.Write the class Square that inherits from Rectangle:
   
    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/square.py

   * 11. Update the class Square by adding the public getter and setter size

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/square.py

   * 12. Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/square.py

   * 13. Rectangle instance to dictionary representation

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/rectangle.py

   * 14. Update class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:This dictionary must contain id, size, x, y

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/square.py

   * 15. Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py

   * 16. Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py

   * 17.Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py

   * 18.Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py

   * 19. Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

    Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0C-python-almost_a_circle
    File: models/base.py

---

## Available methods

/ method name / Description /
---         / ---         /
def __init__(self, id=None) / constructor for Base, rectangle and square class
def to_json_string(list_dictionaries) / convert to JSON string representation
def save_to_file(cls, list_objs)  / write the json string to a file
def from_json_string(json_string) / convert json string to python object
def create(cls, **dictionary)  / returns an instance with all attributes
def load_from_file(cls) / returns a lsit of instances
def save_to_file_csv(cls, list_objs) / save to csv format
def load_from_file_csv(cls) / function to load csv files
def width(self)   / getter function of width of the rectangle
def width(self, width) / setter function for the width of the rectangle
def height(self)  / getter function for the height of the rectangle
def height(self, height)  / setter function for the height of the rectangle
def x(self)  / getter fucntion for the x coordinate of the rectangle
def x(self, x)   / setter function for the x coordinate of the reactangle
def y(self)  / getter function for the y coordinate of the rectangle
def y(self, y) / setter function for the y coordinate of the rectangle
def area(self) / find the area of the rectangle
def display(self) / display the rectangle
def __str__(self) / string representation of a rectangle and square class
def update(self, *args, **kwargs) / update attributes of a rectangle and square
def to_dictionary(self)  / dictionary represenation of a rectangle and square class
def size(self) / getter function for the size of the square
def size(self, size) / setter function for the size of the square
---

## Examples

``` Area ```:
```
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

beniyaml@ubuntu:~/$ ./3-main.py
6
20
56
```

---

``` Display ```
```
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("========")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
========
##
##

---

``` __str ```
```
beniyaml@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

beniyaml@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
beniyaml@ubuntu:~/$ 
```
----


## Author
* **Beniyam Legesse** - [beniyaml] from github account  https://github.com/beniyaml

