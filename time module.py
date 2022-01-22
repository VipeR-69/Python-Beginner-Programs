# epoch = when your computer thinks time began (reference point)

import time

print(time.ctime(0))      # converts a time expressed in seconds since epoch to a readable string


print(time.time())        # return current seconds since epoch

print(time.gmtime())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S" , time_object)
print(local_time)

time_string = "20 April, 2021"
time.strptime(time_string, "%d %B, %Y")
print(time_object)

time_tuple = (2021, 4, 23, 4, 45, 9, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2021, 4, 23, 4, 45, 9, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)