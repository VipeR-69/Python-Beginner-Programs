# zip(iterables) - aggregate elements from two or more iterables (list, tuple, sets, etc.)
#                  creates a zip object with paired elements stored in tuples for each element


usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "admin")
login_date = ["1/1/2022", "3/1/2022", "10/1/2022"]

users = zip(usernames,passwords)
print(type(users))
for i in users:
    print(i)

users = list(zip(usernames,passwords))
print(type(users))
for i in users:
    print(i)

users = dict(zip(usernames,passwords))
print(type(users))
for key,value in users.items():
    print(key+" : "+value)


users = zip(usernames,passwords,login_date)
print(type(users))
for i in users:
    print(i)