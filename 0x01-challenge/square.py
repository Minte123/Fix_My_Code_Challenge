#!/usr/bin/python3
"""
Square module
"""


class Square():

    """ Square object Representation"""
    def __init__(self, *args, **kwargs):
        """ initialize new square object"""
        self.__width = 0
        self.__height = 0
        for key, value in kwargs.items():
            if key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            else:
                setattr(self, key, value)

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        try:
            float(value)
        except TypeError:
            pass
        else:
            if float(value) >= 0:
                self.__width = float(value)

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height"""
        try:
            float(value)
        except TypeError:
            pass
        else:
            if float(value) >= 0:
                self.__height = float(value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Get permiter_of_my_square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):

        """ str representation of square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
