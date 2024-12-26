import threading
import time

lock = threading.Lock()


def high_priority_worker():
    while True:
        with lock:
            print("High-priority worker is working")
            time.sleep(0.1)


def low_priority_worker():
    while True:
        if lock.acquire(blocking=False):  # Низкоприоритетный поток пытается получить доступ
            try:
                print("Low-priority worker is working")
            finally:
                lock.release()
        else:
            print("Low-priority worker is starving")
        time.sleep(0.2)


# Запуск потоков
high_priority_thread = threading.Thread(target=high_priority_worker, daemon=True)
low_priority_thread = threading.Thread(target=low_priority_worker, daemon=True)

high_priority_thread.start()
low_priority_thread.start()

time.sleep(3)  # Даем поработать потокам
