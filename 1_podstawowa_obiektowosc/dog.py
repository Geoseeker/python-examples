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

class Dog(Pet):
    breed = ""
    
    def __init__(self, name, age, owner, breed):
        super(Dog, self).__init__(name, age, owner)
        self.breed = breed

    def bark(self):
        print("Woof woof")

    def giveVoice(self):
        print("woof")

class Cat(Pet):
    
    def miau(self):
        print("Miau miau")

    def giveVoice(self):
        print("miau")


p = Pet("zwierz", 26, "Alicja")


pet = Dog("Burek", 3, "Alicja", "Terrier")

print(pet.name)
print(pet.breed)

pet.eat("ham")
pet.bark()

