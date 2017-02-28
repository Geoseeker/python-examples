from dice import Dice

dice = Dice(8)
print(dice.roll())

# Dice.printPossibleTypes()

tenRolls = dice.rollTenTimes()
for r in tenRolls:
    print("Wyrzucono {}".format(r))
