# from _typeshed import StrPath
import time
import threading

start = time.perf_counter()

def do_something():
    while True:
        print('sleeping 1 seg...')
        time.sleep(2)
        print('Done sleeping')
        print(str(threading.current_thread()))

t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

t1.start()
# t2.start()

finish = time.perf_counter()
while True:
    print('main thread')
    print(str(threading.current_thread()))
    time.sleep(2)
print(f' Finished in {round(finish-start,2)} second(s)')
