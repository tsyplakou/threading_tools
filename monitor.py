import threading
import time
import random


class MonitorQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
        self.condition = threading.Condition()  # Условная переменная

    def produce(self, item):
        with self.condition:  # Захват монитора
            while len(self.queue) >= self.max_size:
                print("Queue is full. Producer is waiting.")
                self.condition.wait()  # Ждём, пока в очереди освободится место
            self.queue.append(item)
            print(f"Produced: {item}")
            self.condition.notify()  # Уведомляем потребителя

    def consume(self):
        with self.condition:  # Захват монитора
            while not self.queue:
                print("Queue is empty. Consumer is waiting.")
                self.condition.wait()  # Ждём, пока в очереди появятся данные
            item = self.queue.pop(0)
            print(f"Consumed: {item}")
            self.condition.notify()  # Уведомляем производителя
            return item


# Создаём монитор
monitor_queue = MonitorQueue(max_size=2)

# Функция производителя
def producer():
    for _ in range(10):
        item = random.randint(1, 100)
        time.sleep(random.uniform(0.5, 1.5))  # Имитация времени производства
        monitor_queue.produce(item)

# Функция потребителя
def consumer():
    for _ in range(10):
        time.sleep(random.uniform(0.5, 2))  # Имитация времени обработки
        monitor_queue.consume()

# Создаём потоки
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Запускаем потоки
producer_thread.start()
consumer_thread.start()

# Ожидаем завершения потоков
producer_thread.join()
consumer_thread.join()

print("All items have been produced and consumed.")
