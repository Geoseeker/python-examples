from advancedCalculator import AdvancedCalculator
from calculator import Calculator
from circle import Circle


print("-------- AdvancedCalculator -------")
cal = Calculator()
cal2 = Calculator()

cal.add(1,1)
cal.add(2,2)
cal2.add(10000, 10000)

advCal = AdvancedCalculator()

advCal.pow(2, 10)
advCal.root(2, 2)
advCal.printOperations()


print("-------- CIRCLE --------")
c = Circle(1, 2, "red", 4)
c.printShape()

area = c.area()
print("Area = " + str(area))
circuit = c.circuit()
print("Circuit = " + str(circuit))
