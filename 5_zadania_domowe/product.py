class Product(object):

        __id = None
        __name = None
        __description = None
        __price = None
        __quantity = None

        __next_id = 1

        def __init__(self, name, description, price, quantity):
            self.__id = Product.__next_id
            Product.__next_id += 1

            self.__name = name
            self.__description = description
            self.__price = price
            self.__quantity = quantity

        def getId(self):
            return self.__id

        def getQuantity(self):
            return self.__quantity

        def setQuantity(self, newQuantity):
            self.__quantity = newQuantity

        def getTotalSum(self):
            totalSum = self.__price * self.__quantity
            if self.__quantity >= 3:
                totalSum -= totalSum * 0.2
            return totalSum
 
        def getProductInfo(self):
            return "{} {} {} {} {} {}".format(self.__id, self.__name, self.__description, self.__quantity, self.__price, self.getTotalSum())


# class FreshProduct(Product):

#     __ex_date = None
