#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ A class that forms a Rectangle

    args: width and height

    args must be argument if not raise value error
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ height for class value Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height property setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Find the area oof a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ Find the perimeter of tye rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ Print string representation in official format """
        p = ""
        if self.width == 0 or self.height == 0:
            return p
        else:
            for row in range(self.height):
                for column in range(self.width):
                    if isinstance(self.print_symbol, list):
                        p += str(self.print_symbol)
                    else:
                        p += self.print_symbol
                p += "\n"
        return p

    def __repr__(self):
        """ Print string representation in official format using repr """
        p = ""
        if self.width == 0 or self.height == 0:
            return p
        else:
            return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Destructor  method to remove instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method accessible by instances of the class or obj """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area == rect_2.area:
            return rect_1
