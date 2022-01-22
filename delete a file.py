import os
import shutil

path = "test"

try:
    #os.remove(path)                  #delete a file
    os.rmdir(path)                   #delete an empty directory
    #shutil.rmtree(path)              #delete a directory containing files

except FileNotFoundError:
    print("that file not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+" was deleted")