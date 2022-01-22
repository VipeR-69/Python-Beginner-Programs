#tuple - collection which is ordered and unchangeable used to group together related data

student = ("chiyari",34,"chiyari","nashe",45)

print(student.index("chiyari"))
print(student.count("chiyari"))

for i in student:
    print(i)

if "chiyari" in  student:
    print("chiyari is here")