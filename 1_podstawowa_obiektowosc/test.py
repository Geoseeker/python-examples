from calculator import Calculator
from shape import Shape

print("------- TEST Calculator -------")
cal = Calculator()


print(cal.add("2","2"))
print(cal.multiply(2,10))
print(cal.subtract(100, 99))

print(cal.divide(10, 0))

print(cal.divide2(10, 2))

cal.printOperations()


print("------- TEST Shape -------")

x = 0
y = 5

shape = Shape(1, 2, "red")
shape1 = Shape(1, "two", "red")
shape2 = Shape(2, 1, 3)
shape3 = Shape("asdas", "asdas", "red")
shape4 = Shape(x, y, "red")

distance = shape.distance(shape2)
print(distance)

# Shape.printShape(s) # zle

shape.printShape()  # dobrze 
print(shape.printShape())
shape.distance(shape2)

