from car import Car

car1 = Car("Chevy","Corvette",2021,"Blue")
car2 = Car("Audi","A5",2021,"Blue")

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)

car1.drive()
car2.stop()