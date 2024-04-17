import threading
import random
import time
import logging

# Configure the logger to include:
# - the message level,
# - the name of the thread in which the log was created
# - the log message itself
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-9s) %(message)s',)


def random_sleeper() -> None:
    sleep_length = random.randint(0, 20)
    logging.debug(f'Starting to sleep for {sleep_length}')
    time.sleep(sleep_length)
    logging.debug('Exiting')


# Create three threads that run the random_sleeper function, each with a different name
t1 = threading.Thread(name="Thread 1", target=random_sleeper)
t2 = threading.Thread(name="Thread 2", target=random_sleeper)
t3 = threading.Thread(name="Thread 3", target=random_sleeper)

# Start all of the threads (set them running)
t1.start()
t2.start()
t3.start()
