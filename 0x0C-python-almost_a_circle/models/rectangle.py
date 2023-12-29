#!/usr/bin/python3
""" Project for *arg and **kwarg """
from models.base import Base


class Rectangle(Base):
    """
    A class for rectangles, inheriting from Base.
    """

    def __init__(self, width, height, x = 0, y = 0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Property getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Property getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Public method to find Area of Rectangle """

        return self.width * self.height

    def display(self):
        """ Prints # to stdout """

        for x in range(self.y):
            print()
        for h in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                w = "#"
                print(w, end="")
            print()

    def __str__(self):
        """ Update Rectangle to print str """
        id_t = self.id
        x_t = self.x
        y_t = self.y
        wd_t = self.width
        ht_t = self.height

        return \
            f"[Rectangle] ({id_t}) {x_t}/{y_t} - {wd_t}/{ht_t}"

    def update(self, *args, **kwargs):
        """
        Update Rectangle with *args
        Take Note of order as is no key word

        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args[:5]):
                setattr(self, attributes[i], arg)
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to Return Dictionary Representation of attributes
        """

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
