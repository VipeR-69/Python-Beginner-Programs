#args - parameter that will apck all arguments into a tuple .
#       useful so that a function can accept a varying amount of arguments.


def add(*anyname):
    sum = 0
    anyname = list(anyname)
    anyname[0] = 0
    for i in anyname:
       sum += i
    return sum

a = add(1,2,3,4,5,6,7)
print(a)
