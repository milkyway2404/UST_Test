import time
import threading

from frequency import *
from circ_queue import *
from passwd import *

def some_task():
    program1()
    program2()
    program3()
    print("Finished task")
if __name__ == "__main__":
    start = time.time()
    # Create thread
    t1 = threading.Thread(target=some_task)
    # Start running thread
    t1.start()
    # Wait until thread is complete, and join the process
    t1.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")
