import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return (f"Done Sleeping...{seconds} seconds")

if __name__ == "__main__":
    
    t1 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:

        # submit method schedules a function to be executed and returns a future object
        # a future object encapsulates the execution of our function and allows us to check on it
        # after it's been scheduled
        f1 = executor.submit(do_something, 1)
        # result method waits until the function is completed
        print(f1.result())

    print("\n", "############ running multiple processes ############")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]

        results = [executor.submit(do_something, sec) for sec in secs]

        # as completed gives us an iterator we can loop over that will yield the result of
        # processes as they are completed
        for result in concurrent.futures.as_completed(results):
            print(result.result())

    print("\n", "############ using the map method ############")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]

        # map runs the function with every item of the list argument
        # instead of returning results as they are completed, as we saw before,
        # map is going to return the results in the order they were started
        results = executor.map(do_something, secs)

        # the results of processes are automatically joined after the context manager ends
        for result in results:
            print(result)

    t2 = time.perf_counter()

    print(f"Process finished in {t2-t1} seconds")



