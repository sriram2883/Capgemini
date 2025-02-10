import threading
import time


def task(lock):
    with lock:
        print("Acquired lock")
        time.sleep(2)
        print("Released lock")


lock = threading.Lock()

thread = [threading.Thread(target=task, args=(lock,)) for _ in range(3)]

for t in thread:
    t.start()

for t in thread:
    t.join()

print("All threads are done")
