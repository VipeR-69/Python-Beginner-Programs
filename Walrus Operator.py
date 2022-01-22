#Walrus Operator ( := )

# new to python 3.8
# assignment expresssion aka walrus operator
# assigns values to a variable as part of a larger expression

happy = True                 #Normal assignment
print(happy)


print(happy := True)     #assignment using Walrus Operator

'''foods = list()
while True:
    food = input("what foof do you like = ")                  #normal program
    if food == "quit":
        break
    foods.append(food)

print(foods)'''


foods = list()
while food := input("Which food do you like - ") != "quit" :                     #same program using walrus operator
    foods.append(food)