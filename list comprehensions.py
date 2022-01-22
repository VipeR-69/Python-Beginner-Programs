# list comprehensions - a way to create a new list with less syntax
#                       can mimic certain lambda functions , easier to read
# SYNTAX - 
#         list = [expression for item in iterable]


squares = []                      # create an empty list
for i in range(1,11):             # create a for loop
    squares.append(i*i)           # define what each loop iteration should do
print(squares)

square = [i*i for i in range(1,11)]          #List Comprehension
print(square)

students = [100,90,80,70,60,50,40,30,0]

pass_students = list(filter(lambda x: x>=60 , students))      #normal
print(pass_students)


passed_stud = [i for i in students if i >= 60]           #list comperhension
print(passed_stud)

passed_stud = [i if i >= 60 else "FAILED" for i in students]     #list comprehension
print(passed_stud)