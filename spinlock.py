import threading
import time


class Spinlock:
    def __init__(self):
        self.lock = threading.Lock()
        self.is_locked = False

    def acquire(self):
        while True:
            with self.lock:
                if not self.is_locked:
                    self.is_locked = True
                    return
            # Поток активно "крутится" в ожидании
            time.sleep(0.001)  # Небольшая задержка для снижения нагрузки

    def release(self):
        with self.lock:
            self.is_locked = False


# Общий ресурс
counter = 0
spinlock = Spinlock()


def increment():
    global counter
    for _ in range(10000):
        spinlock.acquire()
        counter += 1
        spinlock.release()

# Запуск потоков
threads = [threading.Thread(target=increment) for _ in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter value: {counter}")


# Объяснение:
# Потоки пытаются захватить Spinlock через метод acquire.
# Если блокировка занята, поток переходит в цикл ожидания.
# После освобождения блокировки поток, ожидающий захватить её, получает доступ.