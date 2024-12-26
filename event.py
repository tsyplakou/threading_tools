import threading
import time

# Создаём событие
event = threading.Event()


def worker():
    while True:  # Бесконечный цикл
        print("Worker: Waiting for event...")
        event.wait()  # Ожидаем, пока событие не будет установлено
        print("Worker: Event is set, resuming work!")


def setter():
    while True:  # Бесконечный цикл
        print("Setter: Preparing to set event...")
        time.sleep(2)  # Имитация работы
        event.set()  # Устанавливаем событие
        event.clear()  # Сбрасываем событие (если оно было установлено ранее)
        print("Setter: Event is set!")


# Запуск потоков
worker_thread = threading.Thread(target=worker)
setter_thread = threading.Thread(target=setter)

worker_thread.start()
setter_thread.start()

worker_thread.join()
setter_thread.join()

# Объяснение:
#
# Поток worker блокируется на вызове event.wait(), пока событие не будет установлено.
# Поток setter через 3 секунды устанавливает событие с помощью event.set().
# Поток worker разблокируется и продолжает выполнение.
