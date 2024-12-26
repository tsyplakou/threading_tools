import threading
import time

# Семафор с максимальным числом потоков = 2
semaphore = threading.Semaphore(2)


def worker(worker_id):
    print(f"Worker {worker_id} is waiting to access the resource")
    with semaphore:  # Захватываем семафор
        print(f"Worker {worker_id} has accessed the resource")
        time.sleep(2)  # Симуляция работы
    print(f"Worker {worker_id} has released the resource")


# Создаём и запускаем потоки
threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
