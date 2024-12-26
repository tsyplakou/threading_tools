import threading
import queue

class FairLock:
    def __init__(self):
        self.lock = threading.Lock()
        self.wait_queue = queue.Queue()

    def acquire(self):
        # Создаём локальную блокировку для потока
        local_lock = threading.Lock()
        local_lock.acquire()

        # Добавляем эту блокировку в очередь ожидания
        self.wait_queue.put(local_lock)

        # Захватываем основную блокировку, чтобы проверить порядок
        with self.lock:
            # Если текущий поток первый в очереди, отпускаем его локальную блокировку
            if self.wait_queue.queue[0] == local_lock:
                local_lock.release()

        # Ждём, пока локальная блокировка не будет отпущена
        local_lock.acquire()

    def release(self):
        # Удаляем текущий поток из очереди
        with self.lock:
            if not self.wait_queue.empty():
                self.wait_queue.get()

                # Если в очереди есть ещё потоки, отпускаем следующий
                if not self.wait_queue.empty():
                    next_lock = self.wait_queue.queue[0]
                    next_lock.release()



import time

fair_lock = FairLock()

def worker(thread_id):
    for _ in range(2):
        print(f"Thread {thread_id} is trying to acquire the lock")
        fair_lock.acquire()
        print(f"Thread {thread_id} has acquired the lock")
        time.sleep(1)  # Симуляция работы
        fair_lock.release()
        print(f"Thread {thread_id} has released the lock")
        time.sleep(0.5)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All threads have finished.")
