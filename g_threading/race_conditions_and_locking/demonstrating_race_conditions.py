import time
import logging
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

log_format = "%(threadName)s - %(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")


class Counter:
    logger = logging.getLogger(__name__)

    def __init__(self, max_value: int | float):
        if not isinstance(max_value, int) and not isinstance(max_value, float):
            Counter.logger.error(f"Inappropriate type supplied for max_value: {type(max_value)} : {max_value}")
            raise TypeError("Value must be numeric")

        if max_value < 0:
            Counter.logger.error(f"Inappropriate value supplied for max_value: supplied {max_value} but > 0 required")
            raise ValueError("Maximum value must be >= 0")

        self.max_value = max_value
        self.value = 0

    def increment(self, id_num: int) -> None:
        # Set name of thread currently running this counter
        this_thread = current_thread()
        this_thread.name = f"Thread {id_num}"

        Counter.logger.info(f"Beginning increment action - Value: {self.value}")
        time.sleep(0.1)
        local_value = self.value
        local_value += 1
        time.sleep(0.1)
        self.value = local_value
        Counter.logger.info(f"Ending increment action - Value: {self.value}")


if __name__ == "__main__":
    counter = Counter(15)

    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(20):
            executor.submit(counter.increment, i)
