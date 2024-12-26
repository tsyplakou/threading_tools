import threading
import time

# Создаем два Lock (мьютекса)
lock1 = threading.Lock()
lock2 = threading.Lock()

# Функция для первого потока
def thread1():
    print("Thread 1: Trying to acquire lock1")
    with (lock1, lock2):
        print("Thread 1: Acquired lock1")
        time.sleep(1)  # Имитация выполнения операции
        print("Thread 1: Trying to acquire lock2")
        # with lock2:
        #     print("Thread 1: Acquired lock2")
    print("Thread 1: Done")

# Функция для второго потока
def thread2():
    print("Thread 2: Trying to acquire lock2")
    with (lock1, lock2):
        print("Thread 2: Acquired lock2")
        time.sleep(1)  # Имитация выполнения операции
        print("Thread 2: Trying to acquire lock1")
        # with lock1:
        #     print("Thread 2: Acquired lock1")
    print("Thread 2: Done")

# Создаем два потока
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

# Запускаем потоки
t1.start()
t2.start()

# Ждем завершения потоков
t1.join()
t2.join()
