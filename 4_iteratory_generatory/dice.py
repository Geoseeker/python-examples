from random import randint

class Dice(object):

    __diceType = None
    __possibleTypes = [3, 4, 6, 8, 10, 12, 20, 100]

    def __init__(self, diceType):
        if diceType in self.__possibleTypes:
            self.__diceType = diceType
        else:
            raise Exception

    def roll(self):
        return randint(1, self.__diceType)

    def rollTenTimes(self):
        for i in range(10):
            yield self.roll()

    @staticmethod
    def printPossibleTypes():
        for i in Dice.__possibleTypes:
            print(i)

