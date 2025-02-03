import threading
import time
data=[
    list(range(1,100)),
    list(range(10000000,30000000)),
    list(range(30000000,50000000)),
]

def process(data,i):

    start=time.time()
    print(f"Sum of {data[0]} to {data[-1]} is {sum(data)}")
    end=time.time()
    print(f"Thread {i} took {end-start} ns")

threads = []
i=0
for d in data:
    i+=1
    thread = threading.Thread(target=process,args=(d,i))
    threads.append(thread)
    thread.start()
    

for thread in threads:
    thread.join()

print("All threads are done")
