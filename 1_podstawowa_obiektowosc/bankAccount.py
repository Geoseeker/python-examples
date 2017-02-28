
class BankAccount(object):

    __number = None
    __cash = None

    def __init__(self, number):
        self.__number = number
        self.__cash = 0.0


    def getNumber(self):
        return self.__number

    def getCash(self):
        return self.__cash

    # def setNumber(self, newNumber):
    #     self.__number = newNumber

    def depositCash(self, amount):
        if type(amount) is float or type(amount) is int:
            if amount > 0:
                self.__cash += amount
            else:
                print("Given amount <= 0")
        else:
            print("Given amount is not a number")


    def withdrawtCash(self, amount):
        if type(amount) is float or type(amount) is int:
            if amount > 0:
                if amount > self.__cash:
                    amount = self.__cash
                self.__cash -= amount
                print("withdrawtCash: {}".format(amount))
                return amount
            else:
                print("Given amount <= 0")
        else:
            print("Given amount is not a number")

    def printInfo(self):
        print("Number: {}  Cash: {}".format(self.__number, self.__cash))
