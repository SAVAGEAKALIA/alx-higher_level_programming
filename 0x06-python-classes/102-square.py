#!/usr/bin/python3
class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size value.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality operator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Override the not equal operator."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Override the less than operator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Override the less than or equal operator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Override the greater than operator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Override the greater than or equal operator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
