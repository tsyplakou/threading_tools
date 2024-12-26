import threading
import time

orders = [
    'grilled cheeseburger',
    'grilled fish and chips',
    'grilled meat',
]

refrigerator = threading.Lock()
pan = threading.Semaphore(2)
waiter = threading.Semaphore(4)


class Restaurant:
    def cook_order(self, order):
        pass

    def delivery_order(self, order):
        with waiter:
            print(f"Delivering {order}")
            time.sleep(1)  # Simulating delivery time

    def _cook_cheeseburger(self):
        with pan:
            print("Cooking grilled cheeseburger")
            time.sleep(1)  # Simulating cooking time

    def _cook_fish_and_chips(self):
        with pan:
            print("Cooking grilled fish and chips")
            time.sleep(1)  # Simulating cooking time

    def _cook_meat(self):
        with pan:
            print("Cooking grilled meat")
            time.sleep(1)  # Simulating cooking time

    def get_product_from_refrigerator(self, order):
        with refrigerator:
            print(f"Getting {order} from refrigerator")
            time.sleep(1)  # Simulating retrieval time
