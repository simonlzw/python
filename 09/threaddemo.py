import threading
import time


def say_hi():
    time.sleep(3)
    print("Hello World!")

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=say_hi())
        t.start()