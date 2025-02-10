import threading
import time
stop = threading.Event()


def threadd(stop):
    for i in range(10):
        if (stop.is_set()):
            break
        print("thread", i)
        time.sleep(1)


thread1 = threading.Thread(target=threadd, args=(stop,))
thread1.start()

for i in range(10):
    if (i == 6):
        stop.set()
        thread1.join()
    print("main", i)
    time.sleep(1)
