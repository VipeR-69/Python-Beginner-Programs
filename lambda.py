# Lambda Functions - functions written in 1 line using lambda keyword
#                                  accepts any number of arguments , but only has one expression 
#                                  (think of it as a shortcut)
#                                  (useful if needed for a short period of time , throw-away)
#
#   SYNTAX - 
#                  lambda parameters : expression

def double(x):                                   # Normal Function
    return x*2
print(double(5))


double = lambda x : x*2                  # Lambda Fucntion
print(double(5))                                #single parameter

multiply = lambda x,y : x*y               #two parameters
print(multiply(10,5))

add = lambda x,y,z : x+y+z              # three parameters
print(add(5,6,7))

full_name = lambda first_name , last_name : first_name+" "+last_name
print(full_name("Captains","Esports"))

age_check = lambda age : True if age >= 18 else False
print(age_check(18))