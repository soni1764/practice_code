from functools import reduce
# def my_decorator(fun):
#     def wraaper(a, b):
#         print("Welcome")
#         fun(a, b)
#         print("Good Bye")
#
#     return wraaper


# @my_decorator
# def function_to_do():
#     print("do something")
#
#
# function_to_do_ = my_decorator(function_to_do)
#
# function_to_do_()

# @my_decorator
# def add_(a, b):
#     print("doing sum here in actual funtion now")
#     print(a+b)


# sum_ = my_decorator(add_)
# sum_(2, 3)


# def swap_deco(fun):
#     def wrapper(a, b):
#         if a < b:
#             a, b = b, a
#         fun(a, b)
#     return wrapper
#
#
# @swap_deco
# def divide_(a, b):
#     print(a-b)
#
#
# divide_(10, 50)


# ----------------------------read csv---------------------
# import csv
#
# with open("test.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         username = row[0]
#         password = row[1]

# ---------------------------lamda/map/filter/reduce--------------------------------------
#
# mul = lambda a: a*a
# even = lambda a: a % 2 == 0
# add = lambda a, b: a + b
# # print(mul(2, 3))
# nums = [1, 2, 3, 4, 5]
# mul_nums = reduce(add, list(filter(even, list(map(mul, nums)))))
#
# print(mul_nums)


# -----------------------------shallow/deep/copy---------------------------
# import copy
#
# original_copy = [[1, 2, 3], [4, 5, 6]]

# shallow_c = copy.copy(original_copy)

# print(original_copy)
# print(shallow_c)
# shallow_c[0][0] = 'x'
# print(original_copy)
# print(shallow_c)

# deep_c = copy.deepcopy(original_copy)
# print(original_copy)
# print(deep_c)
# deep_c[0][0] = 'x'
# print(original_copy)
# print(deep_c)


# ----------------------------pickle/unpickle--------------------------------
# import pickle
# data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
#
# with open("data.pkl", 'wb') as f:
#     # serialize
#     pickle.dump(data, f)
#
#
# with open("data.pkl", "rb") as f:
#     # deserialize
#     d = pickle.load(f)
#     print(d)


# ---------------------------------asyn call---------------------
# import requests


# def fetch_(url):
#     response = requests.get(url)
#     return response.text
#
#
# def main():
#     print("wait until print me first")
#     print(fetch_("https://www.google.com/"))
#     print("print response before printing me")


# main()


# -------------------------------

# import asyncio
#
#
# async def func1():
#     print("funtion 1 started")
#     await asyncio.sleep(3)
#     print("funtion 1 ended")
#
#
# async def func2():
#     print("function 2 started")
#     await asyncio.sleep(2)
#     print("function 2 ended")
#
#
# async def func3():
#     print("function 3 started")
#     await asyncio.sleep(1)
#     print("function 3 ended")
#
#
# async def main():
#     l = await asyncio.gather(
#         func1(),
#         func2(),
#         func3()
#     )
#     print("main ended")
#
# asyncio.run(main())


# ----------------------------------------

# import asyncio
# import aiohttp


# async def fetch_(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as res:
#             return await res.text()
#
#
# async def main_():
#     res = await fetch_("https://www.verint.com/")
#     print(res)
#
#
# asyncio.run(main_())


# ---------------------------------------
import asyncio
import aiohttp


# async def fetch_(session, url):
#     async with session.get(url) as res:
#         return await res.text()
#
#
# async def main_():

    # async with aiohttp.ClientSession() as session:
    #     res = await fetch_(session, "https://www.verint.com/")
    #     print(res)

    # urls = ["https://www.verint.com/",
    #         "https://www.google.com/",
    #         "https://www.facebook.com/"
    #         ]
    # async with aiohttp.ClientSession() as session:
    #     # tasks = []
    #     # for url in urls:
    #     #     task = await fetch_(session, url)
    #     #     tasks.append(task)
    #
    #     tasks = [fetch_(session, url) for url in urls]
    #
    #     res = await asyncio.gather(*tasks)
    #     print(res)

#
# asyncio.run(main_())


# -------------------------Multiprocessing---------------------------------------------------------------
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

# -------------------------Multithreading-------------------------------------------------
# import threading
# import time
#
#
# def task1(name):
#     print(f"Hello {name}, starting thread 1")
#     time.sleep(5)
#     print("thread 1 completed")
#
#
# def task2(name):
#     print(f"Hello {name}, starting thread 2")
#     time.sleep(2)
#     print("thread 2 completed")
#
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=task1, args=("Soni", ))
#     t2 = threading.Thread(target=task2, args=("Gourav", ))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("done")


# -------------------------Multithreading----using ThreadPool-------a collection of thread-----------------------
import concurrent.futures
import time


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
    print(f"sum of {a} and {b} is {a+b}")
    print("thread 3 completed")


if __name__ == "__main__":
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    pool.submit(worker1)
    pool.submit(worker2, "soni")
    pool.submit(worker3, 2, 3)

    pool.shutdown(wait=True)

    print("Main thread continue")





