from shape import Shape
import math

class Circle(Shape):
    __r = 0

    def __init__(self, x, y, color, r):
        super(Circle, self).__init__(x, y, color)
        self.__r = r

    def printShape(self):
        super(Circle, self).printShape()
        print("r={}".format(self.__r))
    
    def area(self):
        return math.pi * pow(self.__r, 2)

    def circuit(self):
        return 2 * math.pi * self.__r
