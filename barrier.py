import threading
import time

# Создаём барьер для 3 потоков
barrier = threading.Barrier(3)

def worker(thread_id):
    print(f"Thread {thread_id} is working on the first part")
    time.sleep(thread_id)  # Симуляция работы
    print(f"Thread {thread_id} reached the barrier")
    barrier.wait()  # Ожидаем, пока все потоки достигнут барьера
    print(f"Thread {thread_id} is working on the second part")

# Создаём и запускаем потоки
threads = [threading.Thread(target=worker, args=(i,)) for i in range(6)]

for t in threads:
    t.start()

for t in threads:
    t.join()
