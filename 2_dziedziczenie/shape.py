class Shape(object):
    __x = 0
    __y = 0
    color = ""

    def __init__(self, x, y, color):
        if type(x) is int:
            self.__x = x
        else:
            self.__x = 0

        if type(y) is int:
            self.__y = y
        else:
            self.__y = 0

        if type(color) is str:
            self.color = color
        else:
            self.color = "white"

        print("x={} y={} c={}".format(self.__x, self.__y, self.color))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def printShape(self):
        print("Printing x={} y={} c={}".format(self.__x, self.__y, self.color))

    def distance(self, otherShape):
        x1 = self.__x
        x2 = otherShape.__x
        y1 = self.__y
        y2 = otherShape.__y


        distance = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 1/2)
        return distance
