class Organism:

    alive = True

class Animals(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animals):
    def bark(self):
        print("This dog is barking")