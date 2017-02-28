class Pet(object):
    name = ""
    age = ""
    owner = ""
    isHungry = True

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner


    def giveVoice(self):
        print("mrrrrr")

    def eat(self, food):
        self.isHungry = False
        print("{} eats {}".format(self.name, food))

    def printInfo(self):
        print("Name: {} Age: {} Owner: {}".format(self.name, self.age, self.owner))

class Dog(Pet):
    breed = ""
    
    def __init__(self, name, age, owner, breed):
        super(Dog, self).__init__(name, age, owner)
        self.breed = breed

    @staticmethod
    def printDesc():
        print("Pies to najlepszy przyjaciel czlowieka") 

    @staticmethod
    def takeFromShelter(newOwner):
        dog = Dog("Burek", 3, newOwner, "Kundel")
        return dog

    def bark(self):
        print("Woof woof")

    def giveVoice(self):
        print("woof")

    def isTheBest(self):
        return self.age == 1

class Cat(Pet):

    lives = 9

    def die(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            print("zombieeee")
    
    @property
    def isDead(self):
        # if self.lives == 0:
        #     return True
        # else:
        #     return False
        return self.lives == 0

    @isDead.setter
    def isDead(self, isAlive):
        if isAlive:
            self.lives = 9
        else:
            print("still zombieeee")

    @staticmethod
    def printDesc():
        print("Kot to nie jest najlepszy przyjaciel czlowieka") 


    def miau(self):
        print("Miau miau")

    def giveVoice(self):
        print("miau")

class Shelter(object):

    dogs = []
    cats = []
    __i = 0

    def __init__(self):
        dog1 = Dog("Azor", 2, None, "Kundel")
        dog2 = Dog("Hektor", 10, None, "Kundel")
        dog3 = Dog("Rambo", 1, None, "Terrier")
        self.dogs.append(dog1)
        self.dogs.append(dog2)
        self.dogs.append(dog3)

        cat1 = Cat("Mruczek", 1, None)
        cat2 = Cat("Puszek", 5, None)
        cat3 = Cat("Filemon", 3, None)
        self.cats.append(cat1)
        self.cats.append(cat2)
        self.cats.append(cat3)

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i == len(self.dogs):
            raise StopIteration
        dog = self.dogs[self.__i]
        self.__i += 1
        return dog

    def generateCats(self):
        for cat in self.cats:
            yield cat


    def takeDog(self, dog):
        return self.dogs.remove(dog)

print("----- Shelter -----")
shelter = Shelter()

print("1 iteracja")

theBestDog = None
for dog in shelter:
    if dog.isTheBest():
        theBestDog = dog
    dog.printInfo()

print("The best dog is:")
theBestDog.printInfo()

shelter.takeDog(theBestDog)

print("2 iteracja")
for dog in shelter:
    dog.printInfo()

print("Koty")
print("1 iteracja")

catGenerator = shelter.generateCats()
for cat in catGenerator:
    cat.printInfo()
print("2 iteracja")

catGenerator = shelter.generateCats()
for cat in catGenerator:
    cat.printInfo()

print("-------------------")

p = Pet("zwierz", 26, "Alicja")


pet = Dog("Burek", 3, "Alicja", "Terrier")

print(pet.name)
print(pet.breed)

pet.eat("ham")
pet.bark()



Cat.printDesc()

Dog.printDesc()
myNewDog = Dog.takeFromShelter("Alicja")
myNewDog2 = Dog.takeFromShelter("Alicja")

print(myNewDog.owner)


print("--- Test kota --- ")
cat = Cat("Mruczek", 10, "Alicja")

for i in range(10):
    cat.die()
    print("isDead: {} lives:{}".format(cat.isDead, cat.lives))

print("--- magic ---")
cat.isDead = False
print("isDead: {} lives:{}".format(cat.isDead, cat.lives))

print("--- magic 2 ---")
cat.isDead = True
print("isDead: {} lives:{}".format(cat.isDead, cat.lives))

