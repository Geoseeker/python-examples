from product import Product
from shoppingCart import ShoppingCart

p1 = Product("Mleko", "UHT 2%", 2.5, 2)
p2 = Product("Jaja", "Wiejskie 10 sztuk", 10, 1)
p3 = Product("Ser", "Bialy", 5.99, 5)

for p in (p1, p2, p3):
    print(p.getProductInfo())


shoppingCart = ShoppingCart()
shoppingCart.addProduct(p1)
shoppingCart.addProduct(p2)
shoppingCart.addProduct(p3)


shoppingCart.changeProductQuantity(1, 3)
shoppingCart.printReceipt()

