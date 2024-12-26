import queue
import threading
import time

# Создаём очередь
q = queue.PriorityQueue()


def producer():
    for i in range(5):
        print(f"Producer: Producing item {i}")
        q.put((1, i))  # Добавляем элемент в очередь
        print(f"Producer: Producing item {i+5}")
        q.put((0, i+5))  # Добавляем элемент в очередь
        time.sleep(1)  # Имитация времени производства


def consumer():
    while True:
        item = q.get()  # Извлекаем элемент из очереди
        print(f"Consumer: Consumed item {item}")
        q.task_done()  # Сообщаем, что задача выполнена


# Создаём потоки
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)


# Запускаем потоки
producer_thread.start()
consumer_thread.start()

# Ждём завершения работы производителя
producer_thread.join()

# Ждём, пока очередь будет полностью обработана
q.join()

print("All items have been processed.")
