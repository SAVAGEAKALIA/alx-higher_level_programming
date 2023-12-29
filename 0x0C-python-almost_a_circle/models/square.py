#!/usr/bin/python3
""" Project for *arg and **kwarg """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for rectangles, inheriting from Base.
    """

    def __init__(self, size, x = 0, y = 0, id = None):
        """
        Initialize a Rectangle object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The ID of the rectangle.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def area(self):
        """ Public method to find Area of Rectangle """

        return self.size * self.size

    def display(self):
        """ Prints # to stdout """

        for x in range(self.y):
            print()
        for h in range(self.size):
            for y in range(self.x):
                print(" ", end="")
            for w in range(self.size):
                w = "#"
                print(w, end="")
            print()

    def __str__(self):
        """ Update Rectangle to print str """
        id_t = self.id
        x_t = self.x
        y_t = self.y
        sz_t = self.size

        return f"[Square] ({id_t}) {x_t}/{y_t} - {sz_t}"

    @property
    def size(self):
        """Property getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update Rectangle with *args
        Take Note of order as is no key word

        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
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
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
