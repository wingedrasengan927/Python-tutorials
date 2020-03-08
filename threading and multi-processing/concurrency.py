import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds): 
    print("------------------")
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    # always use return when using multi-threading
    return "Done Sleeping"

# new way of using multi-threading
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit method schedules a function to be executed, and returns a future object
    # a future object basically encapsulates the execution of our function,
    # and allows us to check-in on it after it has been scheduled
    # (like we can check if it's running or if it's done)
    f1 = executor.submit(do_something, 1.5)
    f2 = executor.submit(do_something, 1.5)

    print(f1.result())
    print(f2.result())

print("\n", "############ Multiple functions ##########")
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

print("\n", "######## Using the map method ##########")
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # map runs the function with every value in the list
    # instead of yielding the result as it's completed, like we saw before, 
    # map is going to return the results in the order that they were started *
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

'''
if a function raises an exception, then the exception won't be raised while running a thread, but 
instead, the exception is raised when it's value is retrieved.
'''


finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds")