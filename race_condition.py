import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()  # Синхронизатор для доступа к счетчику из нескольких потоков

    def increment(self):
        with self.lock:  # Блокируем доступ к счетчику для изменения
            current_value = self.value
            time.sleep(0.001)  # Искусственная задержка для усиления эффекта гонки
            self.value = current_value + 1

def worker(counter):
    for _ in range(10000):
        counter.increment()

shared_counter = Counter()
threads = [threading.Thread(target=worker, args=(shared_counter,)) for _ in range(2)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {shared_counter.value}")
print("Expected counter value: 20000")
