import random
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

# Configure the logger to include:
# - the message level,
# - the name of the thread in which the log was created
# - the log message itself
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-9s) %(message)s',)


def random_sleeper(id_num: int) -> None:
    # Get a reference to the current thread running this function
    this_thread = current_thread()
    # Set the current thread's name to be this version's id number
    this_thread.name = id_num

    # Continue with remainder of code as normal
    sleep_length = random.randint(0, 20)
    logging.debug(f'Starting to sleep for {sleep_length}')
    time.sleep(sleep_length)
    logging.debug('Exiting')


with ThreadPoolExecutor(max_workers=3) as executor:
    # Create 5 threads that run the random_sleeper function, each with a different name
    for i in range(5):
        executor.submit(random_sleeper, i)
