import threading
import time


class RWLock:
    def __init__(self):
        self.readers = 0
        self.writer = False
        self.lock = threading.Lock()
        self.read_condition = threading.Condition(self.lock)
        self.write_condition = threading.Condition(self.lock)

    def acquire_read(self):
        with self.lock:
            while self.writer:
                self.read_condition.wait()
            self.readers += 1

    def release_read(self):
        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.write_condition.notify_all()

    def acquire_write(self):
        with self.lock:
            while self.writer or self.readers > 0:
                self.write_condition.wait()
            self.writer = True

    def release_write(self):
        with self.lock:
            self.writer = False
            self.read_condition.notify_all()
            self.write_condition.notify_all()


# Создаём экземпляр RWLock
rwlock = RWLock()
shared_data = 0

# Поток для чтения
def reader(thread_id):
    for _ in range(3):
        rwlock.acquire_read()
        print(f"Reader {thread_id}: Read shared_data = {shared_data}")
        time.sleep(0.5)
        rwlock.release_read()


# Поток для записи
def writer(thread_id):
    global shared_data
    for _ in range(3):
        rwlock.acquire_write()
        shared_data += 1
        print(f"Writer {thread_id}: Wrote shared_data = {shared_data}")
        time.sleep(1)
        rwlock.release_write()


# Создаём потоки
reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(2)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(1)]

# Запускаем потоки
for t in reader_threads + writer_threads:
    t.start()

# Ждём завершения всех потоков
for t in reader_threads + writer_threads:
    t.join()

print("All threads have finished.")
