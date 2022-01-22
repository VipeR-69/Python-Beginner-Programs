class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This Rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Eagle(Animal):
    def fly(self):
        print("This eagle is flying")