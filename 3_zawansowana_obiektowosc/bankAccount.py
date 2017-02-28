
class BankAccount(object):

    __nextAccNumber = 1
     
    def __init__(self):
        self.__number = BankAccount.__nextAccNumber
        BankAccount.__nextAccNumber += 1
        self.cash = 0.0

    def getNumber(self):
        return self.__number

    def getCash(self):
        return self.cash

    # def setNumber(self, newNumber):
    #     self.__number = newNumber

    def depositCash(self, amount):
        if type(amount) is float or type(amount) is int:
            if amount > 0:
                self.cash += amount
            else:
                print("Given amount <= 0")
        else:
            print("Given amount is not a number")


    def withdrawtCash(self, amount):
        if type(amount) is float or type(amount) is int:
            if amount > 0:
                if amount > self.cash:
                    amount = self.cash
                self.cash -= amount
                print("withdrawtCash: {}".format(amount))
                return amount
            else:
                print("Given amount <= 0")
        else:
            print("Given amount is not a number")

    def printInfo(self):
        print("Number: {}  Cash: {}".format(self.__number, self.cash))
