
try:
    with open('/home/ragnar/Python Programs/test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("that file was not found")

text = "saste nashe\nKar lo gaiz"
with open("/home/ragnar/Python Programs/test.txt",'w') as file:
    file.write(text)

a = "onii chan\nkimochi yamate"
with open("/home/ragnar/Python Programs/test.txt",'a') as file:
    file.write(a)