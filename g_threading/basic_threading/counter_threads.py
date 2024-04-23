import time
from threading import Thread
import random


def increasing_counter(thread_id: int, value: int) -> None:
    print(f"Thread {thread_id} - value = {value}")
    i = 0
    while i < value:
        print(f"{thread_id}: {i}\n")
        time.sleep(1)
        i += 1


quantity = int(input("How many counters would you like? "))
for count in range(quantity):
    num = random.randint(0, 10)
    counter_thread = Thread(target=increasing_counter,
                            args=(count, num), daemon=True)
    counter_thread.start()

print("Main program complete.")
