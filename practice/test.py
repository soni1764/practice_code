import threading

from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor


def open_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Title for {url} is: {driver.title}")
    driver.quit()


def using_thread_method(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=open_browser, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def using_thread_pool(urls):

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(open_browser, urls)

    # pool = ThreadPoolExecutor(max_workers=3)
    #
    # for url in urls:
    #     pool.submit(open_browser, url)
    # pool.shutdown(wait=True)


# if __name__ == "__main__":
#     urls_ = ["https://www.google.com/", "https://www.facebook.com/",
#             "https://www.w3schools.com/"]
#
#     # using_thread_method(urls_)
#     using_thread_pool(urls_)






