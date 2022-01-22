#scope = the region that a variable is recognized .
#        a variable is only available from inside the region it is created .
#        a global and  locally scoped variable of a variable can be created .


name = "chiyari"    #global scope (available inside & outside functions)

def display():
    name = "code"           # local scope (available only inside this function)
    print(name)

display()
print(name)