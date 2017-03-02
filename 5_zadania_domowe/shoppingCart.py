class ShoppingCart(object):

    def __init__(self):
        self.__products = []

    def addProduct(self, newProduct):
        self.__products.append(newProduct)

    def removeProduct(self, productIdToRemove):
        for product in self.__products:
            if product.getId() == productIdToRemove:
                self.__products.remove(product)

    def changeProductQuantity(self, productId, newQuantity):
        for product in self.__products:
            if product.getId() == productId:
                product.setQuantity(newQuantity)

    def addProductQuantity(self, productId, addedQuantity):
        for product in self.__products:
            if product.getId() == productId:
                newQuantity = product.getQuantity() + addedQuantity
                product.setQuantity(newQuantity)

    def printReceipt(self):
        totalPrice = 0.0
        print(" -- Receipt -- ")
        for product in self.__products:
            print(product.getProductInfo())
            totalPrice += product.getTotalSum()
        print("Total: {}".format(totalPrice))
        print(" ------------- ")



