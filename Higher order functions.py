# Higher Order Functions     -    a function that either :
#                                                  1. accepts a functionas an argument
#                                                  or
#                                                  2. returns a function
#                                                     (In Python , functions are also treated as objects)

def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):
    text = func(input("enter something - "))
    print(text)

hello(loud)
hello(quite)

#####################################################################

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))