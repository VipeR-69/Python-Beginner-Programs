# daemon thread - a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normallt be killed, stay alive until task is complete
#
#  Ex. - background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for - ",count," seconds")

x = threading.Thread(target=timer)
x.start()

x.setDaemon(True)
print(x.isDaemon())

answer = input("Do you wish to exit ? ")
