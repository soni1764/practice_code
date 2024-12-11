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
from collections import deque
# from collections import

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


# --------------------------call parent class constructor---------------------------
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent class constructor called. Name: {self.name}")


class Child(Parent):
    def __init__(self, name, age):
        # Call the parent class constructor
        super().__init__(name)
        self.age = age
        print(f"Child class constructor called. Age: {self.age}")


# if __name__ == "__main__":
#     # Create an instance of Child
#     child_instance = Child("John", 12)


class Parent1:
    def __init__(self, name):
        self.name = name
        print(f"Parent1 class constructor called. Name: {self.name}")


class Parent2:
    def __init__(self, age):
        self.age = age
        print(f"Parent2 class constructor called. Age: {self.age}")


class Child2(Parent1, Parent2):
    def __init__(self, name, age, grade):
        # Call the parent class constructors
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        self.grade = grade
        print(f"Child class constructor called. Grade: {self.grade}")


# if __name__ == "__main__":
#     # Create an instance of Child
#     child_instance = Child2("Alice", 14, "8th Grade")


# ----------------Binary Search----------------------------------
def binary_search(given_arr, targ):
    low = 0
    high = len(given_arr) -1
    while low <= high:
        mid = (low + high) // 2
        if given_arr[mid] == targ:
            return mid
        elif given_arr[mid] > targ:
            high = mid - 1
        else:
            low = mid + 1
    return -1



# if __name__ == "__main__":
#     # Example usage
#     arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#     target = 7
#     result = binary_search(arr, target)
#     if result != -1:
#         print(f"Element found at index {result}")
#     else:
#         print("Element not found")


# -----------------------Collections---------------------------------------
# ---------------named_tuple-----------------
from collections import namedtuple
def named_tuple():
    Soni = namedtuple("Soni", ['a', 'b'])
    s = Soni(1, 2)
    print(s.a)
    print(s.b)

# if __name__ == "__main__":
#     named_tuple()


# ----------------------deque-------------------------
from collections import deque
def de_queue():
    d = deque()
    d.append(1)
    d.append(2)
    d.append(3)
    print(d.pop())
    print(d.popleft())

# if __name__ == "__main__":
#     de_queue()


# ----------------------Counter-------------------------
from collections import Counter
def Counter_():
    counts = Counter(['a', 'b', 'a', 'c', 'b', 'b'])
    print(counts)
    counts.update(['c'])
    print(counts)

# if __name__ == "__main__":
#     Counter_()


# ----------------------defaultDict-------------------------
from collections import defaultdict
def defaultdict_():
    d = defaultdict(int)
    print(d)
    d['a'] += 1
    d['b'] += 2
    print(d)

    d = defaultdict(list)
    d['a'].append(1)
    d['c'].append(2)
    print(d)

# if __name__ == "__main__":
#     defaultdict_()



# ----------------------OrderedDict-------------------------
from collections import OrderedDict
def OrderedDict_():
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    print(d)

# if __name__ == "__main__":
#     OrderedDict_()


# ----------------------ChainMap-------------------------
from collections import ChainMap
def ChainMap_():
    d1 = {1: 1, 2: 2, 3: 3}
    d2 = {4: 4, 5: 5, 6: 6}
    d = ChainMap(d1, d2)
    print(d[1])
    print(d[4])
    print(d)

# if __name__ == "__main__":
#     ChainMap_()


# ----------------------UserDict, UserList, and UserString-------------------------
from collections import UserDict
class MyDict:
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("Keys must be strings")
        super().__setitem__(key, value)


# if __name__ == "__main__":
#     d = UserDict()
#     d[1] = 1
#     print(d)


# ---------------------queue-----FIFO-------------------
from queue import Queue
def queue_():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.empty())

def queue_2():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())


def queue_3():
    q = []
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.pop(0))
    print(q.pop(0))
    print(q.pop(0))

# if __name__ == "__main__":
#     queue_3()


# ---------------------stack-----LIFO-------------------
from queue import LifoQueue
def stack_3():
    stack = LifoQueue()
    stack.put(1)
    stack.put(2)
    stack.put(3)
    print(stack.empty())
    print(stack.get())
    print(stack.get())
    print(stack.get())
    print(stack.empty())

def stack_():
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack.pop)
    print(stack.pop())
    print(stack.pop())


def stack_2():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    stack_3()