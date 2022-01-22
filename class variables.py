from car import Car

car1 = Car("Mercedes","X5",2021,"Blue")
car2 = Car("BMW","A20",2022,"Black")

car1.wheels = 2

Car.wheels = 6

print(car1.wheels)

print(Car.wheels)

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()