import time
import threading

'''
CPU bound tasks - tasks which use use cpu
                - these can be benefitted rom multiprocessing
I/O bound tasks - tasks which wait for input and output operations to be completed
                - these can be benefitted from threading

- when we actually run something using threads, it's not actually running code at the same time,
  but it gives the illusion of running code at the same time (similar to asynchronous programming)
'''

# start a counter to measure the start time
start = time.perf_counter()

# create a basic sleep function
def do_something():
    print("------------------")
    print("sleeping now...")
    time.sleep(1)
    print("Done Sleeping")
    print("-----------------")

do_something()
do_something()

# measure the finish time
finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds")

# --------------- USING THREADING ----------------
print("\n", "########## using threading #########")

start1 = time.perf_counter()

# create two threads for each of the functions
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target = do_something)

# start the thread
t1.start()
t2.start()

# make sure that both the threads are finished before moving on to the next line
t1.join()
t2.join()

finish1 = time.perf_counter()

print(f"finished in {round(finish1-start1, 2)} seconds")

# --------------- BETTER SYNTAX ----------------
print("\n", "########## better syntax and arguments #########")

start2 = time.perf_counter()

def do_something_2(seconds):
    print("------------------")
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Done Sleeping")
    print("-----------------")

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something_2, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish2 = time.perf_counter()

print(f"finished in {round(finish2-start2, 2)} seconds")