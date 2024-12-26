import threading
import time
import random

# Условная переменная
condition = threading.Condition()

# Общий ресурс
shared_data = []

# Поток производителя
def producer(producer_id):
    for _ in range(5):
        with condition:
            item = random.randint(1, 100)
            shared_data.append(item)
            print(f"Producer {producer_id}: Produced {item}")
            condition.notify()  # Уведомляем одного из потребителей
        time.sleep(random.uniform(0.5, 1.5))

# Поток потребителя
def consumer(consumer_id):
    while True:
        with condition:
            while not shared_data:
                print(f"Consumer {consumer_id}: Waiting for data")
                condition.wait()  # Ждём, пока появятся данные
            item = shared_data.pop(0)
            print(f"Consumer {consumer_id}: Consumed {item}")
        # time.sleep(random.uniform(0.5, 1.0))

# Создаём потоки производителей и потребителей
producer_threads = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumer_threads = [threading.Thread(target=consumer, args=(i,), daemon=True) for i in range(3)]

# Запускаем все потоки
for t in producer_threads + consumer_threads:
    t.start()

# Ожидаем завершения работы производителей
for t in producer_threads:
    t.join()

print("All producers have finished. Consumers will stop after consuming all items.")
time.sleep(5)  # Дадим потребителям завершить работу
