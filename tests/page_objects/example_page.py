from selenium.webdriver.common.by import By


class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.about = (By.XPATH, "//*[text()='About']")

    def get_title(self):
        return self.driver.title

    def get_about_text(self):
        return self.driver.find_element(*self.about).get_attribute('value')
