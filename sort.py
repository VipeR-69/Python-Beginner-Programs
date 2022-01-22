# sort() method - used with lists
# sorted() function - used with iterables

stud = ["harry","chiyari","jadu","cheta","babar"]
students = ("harry","chiyari","jadu","cheta","babar")

a = [ ("Chiyari","F",34),
        ("Jadu","E",45),
        ("Cheta","C",67),
        ("Babar","B",78) ]

b = ( ("Chiyari","F",34),
        ("Jadu","E",45),
        ("Cheta","C",67),
        ("Babar","B",78) )

stud.sort()
for i in stud:
    print(i)

stud.sort(reverse=True)
for i in stud:
    print(i)

sorted_students = sorted(students)
for i in sorted_students:
    print(i)

sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)

grade = lambda grades : grades[1]
a.sort(key = grade)
for i in a:
    print(i)

grade = lambda grades : grades[1]
a.sort(key = grade,reverse = True)
for i in a:
    print(i)

numbers = lambda num : num[2]
a.sort(key = numbers)
for i in a:
    print(i)


numbers = lambda num : num[2]
st = sorted(b,key=numbers)
for i in st:
    print(i)