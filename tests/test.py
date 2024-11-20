# import multiprocessing
# import time
#
#
# def task1(name):
#     print(f"Hello {name}, starting process 1")
#     time.sleep(5)
#     print("process 1 completed")
#
#
# def task2(name):
#     print(f"Hello {name}, starting process 2")
#     time.sleep(2)
#     print("process 2 completed")
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=task1, args=("Soni",))
#     p2 = multiprocessing.Process(target=task2, args=("Gourav",))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("done")

import threading
import time


def task1(name):
    print(f"Hello {name}, starting thread 1")
    time.sleep(5)
    print("thread 1 completed")


def task2(name):
    print(f"Hello {name}, starting thread 2")
    time.sleep(2)
    print("thread 2 completed")


if __name__ == "__main__":
    t1 = threading.Thread(target=task1, args=("Soni", ))
    t2 = threading.Thread(target=task2, args=("Gourav", ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done")
