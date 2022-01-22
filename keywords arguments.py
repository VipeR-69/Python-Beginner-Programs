# Keywords Arguments - arguments preceded by an identifier when we pass them to a function .
#                      the order of the arguments doesn't matter , unlike positional arguments
#                       python knows the names of the arguments that our function recieves.

def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)


hello("naman","delhi","wala")             #positional arguments

hello(last="wala",first="Naman",middle="delhi")             #keywords arguments
