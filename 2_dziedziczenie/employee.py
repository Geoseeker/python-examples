class Employee(object):
    
    __id = None
    __first_name = None
    __last_name = None
    __salary = None

    def __init__(self, newId, first_name, last_name, salary):
        self.__id = newId
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def raiseSalary(self, percent):
        if type(percent) is float or type(percent) is int:
            if percent > 0:
                self.__salary += self.__salary * (percent/100)
            else:
                print("Given percent <= 0")
        else:
            print("Given percent is not a number")

    def printInfo(self):
        print("Id:{} Name:{} Salary:{}".format(self.__id, self.__first_name + " " + self.__last_name, self.__salary))

    def getSalary(self):
        return self.__salary
