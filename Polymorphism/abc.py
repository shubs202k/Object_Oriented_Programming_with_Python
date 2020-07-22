# abc = abstract base class

from abc import ABCMeta, abstractmethod

# For every shape we have method area that calculate area of that shape
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4

    def area(self):
        print("Area of Square : ",self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)


square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()

# cant instantiate abstract class , shape = Shape()
