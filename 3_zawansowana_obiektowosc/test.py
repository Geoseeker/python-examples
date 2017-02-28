from advancedCalculator import AdvancedCalculator
from bankAccount import BankAccount


r = 2
radius = AdvancedCalculator.computeCircleRadius(r)
print("radius = {}".format(radius))

print("--- BankAccount ---")

ba = BankAccount()
ba.printInfo()

ba2 = BankAccount()
ba2.printInfo()

ba3 = BankAccount()
ba3.printInfo()

print("---")
ba.depositCash(100)
ba.printInfo()
ba2.printInfo()

