#Method Chaining - calling multiple methods sequentially.
#                  each call perform an action on the same object and returns self.

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("you turn off the engine")
        return self


car = Car()

car.turn_on()       #Normal calling method
car.drive()         #Normal calling method

car.turn_on().drive()       #Method Chaining
car.brake().turn_off()      #Method Chaining

# Or we can also write it like this in order to make it more readable
# with the help of line continuation character (\)
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()