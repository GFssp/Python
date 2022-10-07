from multiprocessing import Process
from threading import Thread
import os
import time

processes = []
num_processes = os.cpu_count()


def square_numbers(args):
    for i in range(1000):
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # Create processes
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start process
    for thread in threads:
        thread.start()

    # join
    for thread in threads:
        thread.join()

    print('end main')
