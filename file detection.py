import os

path = "/home/ragnar/Python Programs/test.txt"

if os.path.exists(path):
    print("that location exist")
    if os.path.isfile(path):
        print("that is a file")
else:
    print("that location doesn't exist")