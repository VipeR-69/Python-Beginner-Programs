#**************************************
# Python Multiprocessing
#**************************************
#
# multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing - better for cpu bound tasks (heavy cpu usage)
#                   multithreading - better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())
    
    a = Process(target=counter , args=(125000000,))
    b = Process(target=counter , args=(125000000,))
    c = Process(target=counter , args=(125000000,))
    d = Process(target=counter , args=(125000000,))
    e = Process(target=counter , args=(125000000,))
    f = Process(target=counter , args=(125000000,))
    g = Process(target=counter , args=(125000000,))
    h = Process(target=counter , args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("finished in ",time.perf_counter()," seconds")

if __name__ == '__main__':
    main()