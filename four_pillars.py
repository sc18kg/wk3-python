# Four Pilars

# Abstraction
# Hiding the functionality from user using methods to overall making it easier
#
# Encapsulation
# Enclosing/hiding to dangerous things
# 
# Inheritance
# Using super to stop repeating code using other methods to inherit parameters
# 
# Polymorphism
# Methods overwrite when inheriting

class Animal:
    def __init__(self):
        self.alive = True

    def hunt(self):

        print("Searching for food")

    def move(self):
        print("Moving..")    

class Reptile(Animal):
    def __init__(self, reptile_type, colour):
        super().__init__()     #Super class creation for Animal then calls their init for inheritance
        self.type = reptile_type
        self.colour = colour


class Lizard(Reptile):
    def __init__(self, colour):
        super().__init__("Lizard", colour) # As the super class takes two input this has to be initiated


class Mammal(Animal):
    def __init__(self):
        super().__init__()

    def breed(self):
        print("Giving birth to live young")

class Platypus(Mammal):
    def __init__(self):
        super().__init__()
    
    def breed(self):
        print("Platypus lays eggs")

perry = Platypus
perry.breed()


r = Reptile("Lizard", "Blue")
print(r.alive)
r.move()
a = Animal()
a.hunt()
a.move()
l = Lizard("Purple")