class Point:
    x = 0  # static or class variable
    y = 0
    __z = 0  # private variable
    _p = 0  # protected variable

    def show(self):
        print(self.__z, self._p)


class Rectangle:
    def __init__(self, width=0, height=0, corner=None):  # constructor
        self.width = width
        self.height = height  # instance variable
        self.corner = corner

    def __del__(self):  # destructor
        print('destructor or del called')

    @classmethod
    def hello(cls):
        print(cls.__name__)

    @staticmethod
    def hi():
        print('hi')


class Square(Rectangle):
    def __init__(self, width=0, corner=None):
        self.width = self.height = width
        self.corner = corner

        # calling super constructor
        Rectangle.__init__(self, width, width, corner)


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


def grow_rect(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print(Point)
blank = Point()
blank.x = 10
blank.y = 20
print(blank)
print_point(blank)

box = Rectangle()
box.width = 200
box.height = 400
box.corner = Point()
box.corner.x = 0
box.corner.y = 0
center = find_center(box)
print_point(center)
grow_rect(box, 500, 200)
box.hello()
box.hi()

# DATACLASS PYTHON 3.7          instead of __init__

from dataclasses import dataclass
from typing import Any


@dataclass
class cube:
    side: int
    name: str
    extra: Any = "nothing"


myCube = cube(10, "mycube")
print(myCube)
