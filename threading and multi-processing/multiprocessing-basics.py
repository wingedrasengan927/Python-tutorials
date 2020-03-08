import time
import multiprocessing

'''
- In multiprocessing, we're gonna spread the work on multiple processors
- can be used with both I/O bound tasks and CPU bound tasks
- In multi-threading, tasks doesn't have to run at the same time
- In multi-processing, tasks do run at the same time
- even if you don't have multiple cores, your computer has ways of switching off
  between cores when one of them isn't too busy
- Serializing something with pickle means we are converting python object to a format,
  that can be deconstructed and reconstructed in another python script
'''

def do_something():
    print("Sleeping now....")
    time.sleep(1)
    print("Done Sleeping")

def do_something_2(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Done Sleeping")

if __name__ == "__main__":

    t1 = time.perf_counter()

    # create processes
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # start the process
    p1.start()
    p2.start()

    # join the process
    p1.join()
    p2.join()

    t2 = time.perf_counter()

    print(f"Process finished in {t2-t1} seconds")

    print()
    print("########### Multiple Processes ##########")

    t3 = time.perf_counter()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    t4 = time.perf_counter()

    print(f"Process finished in {t4-t3} seconds")

    
    print()
    print("########### Accepting Arguments ##########")

    t5 = time.perf_counter()

    processes = []
    for _ in range(10):
        # unlike threads, in order to pass arguments to a process,
        # the arguments must be able to serialize using pickle
        p = multiprocessing.Process(target=do_something_2, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    t6 = time.perf_counter()

    print(f"Process finished in {t6-t5} seconds")