# **kwargs = prameter that will pack all arguments into a dictionary .
#            useful so that a function can accept a varying amount of keyword arguments .


def hello(**anyname):
    print("hello " + anyname['first'] + " " + anyname['last'])
    print("hello",end=" ")
    for key,value in anyname.items():
        print(value,end = " ")


hello(first="chiyari",middle="maha",last="chutiya")
