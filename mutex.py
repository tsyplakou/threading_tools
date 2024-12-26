import threading

counter = 0
mutex = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with mutex:  # Захват мьютекса
            counter += 1  # Критическая секция


threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
