from concurrent.futures import ThreadPoolExecutor
import random


def increasing_counter(thread_id: int, value: int) -> None:
    print(f"Thread {thread_id} - value = {value}")
    i = 0
    while i < value:
        print(f"{thread_id}: {i}")
        i += 1


quantity = int(input("How many counters would you like? "))
# Create a thread pool executor to manage our jobs
# This will allocate each incoming job to a thread from its pool of "workers"
# This pool has been set up to hold a max of 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:
    for count in range(quantity):
        num = random.randint(0, 10)

        # Add a new job to the thread pool
        # submit replaces the direct call to create a wrapper thread and start it
        # The first parameter is the function to be called
        # All subsequent parameters are for the supplied function
        executor.submit(increasing_counter, count, num)
        # No need for this now!
        #counter_thread = Thread(target=increasing_counter, args=(count, num))
        #counter_thread.start()

print("Main program complete.")
