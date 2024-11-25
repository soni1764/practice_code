from functools import reduce
import csv
import copy
import pickle
import requests
import asyncio
import aiohttp
import multiprocessing
import threading
import time
import concurrent.futures
import pytesseract
from PIL import Image
from itertools import permutations


def my_decorator1(fun):
    def wraaper():
        print("Welcome")
        fun()
        print("Good Bye")

    return wraaper


@my_decorator1
def function_to_do():
    print("do something")


# if __name__ == "__main__":
#     function_to_do_ = my_decorator1(function_to_do)
#     function_to_do_()


def my_decorator2(fun):
    def wraaper(a, b):
        print("Welcome")
        fun(a, b)
        print("Good Bye")

    return wraaper


@my_decorator2
def add_(a, b):
    print("doing sum here in actual funtion now")
    print(a + b)


# if __name__ == "__main__":
#     add_(2,3)
#     # sum_ = my_decorator2(add_)
#     # sum_(2, 3)


def swap_deco(fun):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        fun(a, b)

    return wrapper


@swap_deco
def divide_(a, b):
    print(a - b)

    # if __name__ == "__main__":
    #     divide_(10, 50)

    # ----------------------------read csv---------------------
    # if __name__ == "__main__":
    #     with open("test.csv", "r") as file:
    #         csv_reader = csv.reader(file)
    #         header = next(csv_reader)
    #         for row in csv_reader:
    #             username = row[0]
    #             password = row[1]
    #     print(username, password)

    # ---------------------------lamda/map/filter/reduce--------------------------------------
    # if __name__ == "__main__":
    #     mul = lambda a: a*a
    #     even = lambda a: a % 2 == 0
    #     add = lambda a, b: a + b
    #     print(mul(2))
    #     nums = [1, 2, 3, 4, 5, 6]
    #     print(list(map(mul, nums)))
    #     print(list(filter(even, list(map(mul, nums)))))
    #     mul_nums = reduce(add, list(filter(even, list(map(mul, nums)))))
    #
    #     print(mul_nums)

    # -----------------------------shallow/deep/copy---------------------------
    # if __name__ == "__main__":
    original_copy = [[1, 2, 3], [4, 5, 6]]
    shallow_c = copy.copy(original_copy)

    # print(original_copy)
    # print(shallow_c)
    # shallow_c[0][0] = 'x'
    # print(original_copy)
    # print(shallow_c)

    deep_c = copy.deepcopy(original_copy)
    # print(original_copy)
    # print(deep_c)
    deep_c[0][0] = 'x'
    print(original_copy)
    print(deep_c)


# ----------------------------pickle/unpickle--------------------------------
# if __name__ == "__main__":
#     data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
#
#     with open("data.pkl", 'wb') as f:
#         # serialize
#         pickle.dump(data, f)
#
#     with open("data.pkl", "rb") as f:
#         # deserialize
#         d = pickle.load(f)
#         print(d)


# ---------------------------------asyn call---------------------
def fetch1(url):
    response = requests.get(url)
    return response.text


def main1():
    print("wait until print me first")
    print(fetch1("https://www.google.com/"))
    print("print response before printing me")


# if __name__ == "__main__":
#     main1()


# -------------------------------
async def func1():
    print("funtion 1 started")
    await asyncio.sleep(3)
    print("funtion 1 ended")


async def func2():
    print("function 2 started")
    await asyncio.sleep(2)
    print("function 2 ended")


async def func3():
    print("function 3 started")
    await asyncio.sleep(1)
    print("function 3 ended")


async def main2():
    l_ = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print("main ended")


# if __name__ == "__main__":
#     asyncio.run(main2())

# ----------------------------------------
async def fetch2(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return await res.text()


async def main3():
    res = await fetch2("https://www.verint.com/")
    print(res)


# if __name__ == "__main__":
#     asyncio.run(main3())


# ---------------------------------------
async def fetch3(session, url):
    async with session.get(url) as res:
        return await res.text()


async def main4(url):
    async with aiohttp.ClientSession() as session:
        res = await fetch3(session, url)
        print(res)


async def main5(urls_):

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls_:
            task = await fetch3(session, url)
            tasks.append(task)
    for task in tasks:
        print(task)
        time.sleep(2)
        print()


async def main6(urls_):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch3(session, url) for url in urls_]
        for task in tasks:
            print(task)
            print(time.sleep(2))
            print()
        res = await asyncio.gather(*tasks)
    for r in res:
        print(r)
        print(time.sleep(2))
        print()


# if __name__ == "__main__":
#     # asyncio.run(main4("https://www.verint.com/"))
#     urls = ["https://www.verint.com/",
#             "https://www.google.com/",
#             "https://www.facebook.com/"
#             ]
#
#     # asyncio.run(main5(urls))
#     asyncio.run(main6(urls))


# -------------------------Multiprocessing---------------------------------------------------------------
def task1(name):
    print(f"Hello {name}, starting process 1")
    time.sleep(5)
    print("process 1 completed")


def task2(name):
    print(f"Hello {name}, starting process 2")
    time.sleep(2)
    print("process 2 completed")


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

# -------------------------Multithreading-------------------------------------------------
def task3(name):
    print(f"Hello {name}, starting thread 1")
    time.sleep(5)
    print("thread 1 completed")


def task4(name):
    print(f"Hello {name}, starting thread 2")
    time.sleep(2)
    print("thread 2 completed")


# if __name__ == "__main__":
#     t1 = threading.Thread(target=task3, args=("Soni", ))
#     t2 = threading.Thread(target=task4, args=("Gourav", ))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("done")


# -------------------------Multithreading----using ThreadPool-------a collection of thread-----------------------
def worker1():
    print(f"Hello, starting thread 1")
    time.sleep(5)
    print("thread 1 completed")


def worker2(name):
    print(f"Hello {name}, starting thread 2")
    time.sleep(3)
    print("thread 2 completed")


def worker3(a, b):
    print(f"Hello, starting thread 3")
    time.sleep(2)
    print(f"sum of {a} and {b} is {a + b}")
    print("thread 3 completed")


# if __name__ == "__main__":
#     pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
#     pool.submit(worker1)
#     pool.submit(worker2, "soni")
#     pool.submit(worker3, 2, 3)
#
#     pool.shutdown(wait=True)
#
#     print("Main thread continue")


# -----------------------------get text from image------------------------------------------------------------
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
image_path = "pic.webp"
image = Image.open(image_path)

# if __name__ == "__main__":
#     text = pytesseract.image_to_string(image)
#     print(text)
#     print(text[:-1])


# -----------------------------get permutation of a in b------------------------------------------------------------
def get_per(a):
    for p in permutations(a):
        # print(p)
        print(''.join(p))


def get_per2(a):
    p = [''.join(p) for p in permutations(a)]
    print(p)


def get_per_of_a_in_b(a, b):
    perms = [''.join(p) for p in permutations(a)]
    # ans = [p for p in perms if p in b]
    # print(ans)
    for p in perms:
        if p in b:
            print(p)


# if __name__ == "__main__":
#     small_str = "abc"
#     large_str = "cbabadcbbabbcbabaabccbabc"
# #     get_per(small_str)
# #     get_per2(small_str)
#     get_per_of_a_in_b(small_str, large_str)
