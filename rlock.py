import threading

lock = threading.RLock()


def factorial(n):
    with lock:
        return factorial(n-1) * n if n > 1 else 1


t = threading.Thread(target=factorial, args=(11,))
t1 = threading.Thread(target=factorial, args=(15,))
t.start()
t1.start()
t.join()
t1.join()



lock.acquire(blocking=True)

try:
    # critical section
    pass
finally:
    lock.release()


with lock:
    # critical section
    pass