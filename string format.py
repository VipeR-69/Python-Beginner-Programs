# str.format() =  optional method that given users more control when displaying output
#          {}  =  format field

animal = 'cow'
items = "moon"

print("The {} jumped over the {}".format(animal,items))

print("The {1} jumped over the {0}".format(animal,items))       #positional arguments
 
print("The {a} jumped over the {b}".format(a="cow",b="moon"))    #keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal,items))

name = "chiyari"
print("hello , my name is {}".format(name))
print("hello , my name is {:10}. nice to meet u".format(name))
print("hello , my name is {:<10}. nice to meet u".format(name))   #left alligned
print("hello , my name is {:>10}. nice to meet u".format(name))   #right alligned
print("hello , my name is {:^10}. nice to meet u".format(name))   #center alligned
print("hello , my name is {0:10}. nice to meet u".format(name))


number = 3.14159
print("The number pi is {:.4f}".format(number))

num = 1000
print("the number is {:,}".format(num))
print("the number is {:b}".format(num))       #display as binary
print("the number is {:o}".format(num))       #display as octal
print("the number is {:X}".format(num))       #display as hexa-decimal
print("the number is {:E}".format(num))       #display as scientific notation