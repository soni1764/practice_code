import threading

from selenium import webdriver


def open_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Title for {url} is: {driver.title}")
    driver.quit()


if __name__ == "__main__":
    urls = ["https://www.google.com/", "https://www.facebook.com/",
            "https://www.w3schools.com/"]

    threads = []
    for url in urls:
        thread = threading.Thread(target=open_browser, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

