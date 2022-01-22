# Prevents a user from creating an object of that class
# + compels a user to overwrite abstract methods in a child class

# abstact class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation .

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive a car")

    def stop(self):
        print("This car is stopped")

class Bike(Vehicle):
    def go(self):
        print("you drive a bike")

    def stop(self):
        print("This car is stopped")


#vehicle = Vehicle()
car = Car()
bike = Bike()

#vehicle.go()
car.go()
bike.go()
car.stop()
bike.stop()