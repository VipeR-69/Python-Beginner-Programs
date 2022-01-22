# filter() = creates a collection of elements from an iterable for which a function
#            returns true
# SYNTAX - 
#        filter(function , iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Noah",17),
           ("Minnie",20),
           ("Joey",16),
           ("Joss",21)]

age = lambda data:data[1] >= 18
a = list(filter(age,friends))
for i in a:
    print(i)