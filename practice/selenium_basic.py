import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Demo:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        # time.sleep(5)

    def radio_button(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(self.driver.title)
        # click radio button
        rbs = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
        print(len(rbs))
        for button in rbs:
            print(button.get_attribute("value"))
            print(button.is_selected())
            button.click()
            print(button.is_selected())
        time.sleep(3)

    def static_drop_down(self):
        # click radio button
        sel = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        sel.select_by_value("option2")
        print(self.driver.find_element(By.ID, "dropdown-class-example").text)
        time.sleep(3)

    def check_box(self):
        self.driver.find_element(By.XPATH, "//input[@name='checkBoxOption1']").click()
        cb = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        cb[2].click()
        for i in cb:
            if i.get_attribute("value") == 'option2':
                print(i.is_selected())
                i.click()
                print(i.is_selected())

    def js_alert(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("alert")
        self.driver.find_element(By.ID, "alertbtn").click()
        alert = self.driver.switch_to.alert
        txt = alert.text
        print(txt)
        alert.accept()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("alert")
        self.driver.find_element(By.ID, "confirmbtn").click()
        txt = alert.text
        print(txt)
        alert.accept()
        self.driver.find_element(By.ID, "confirmbtn").click()
        txt = alert.text
        print(txt)
        alert.dismiss()

    def hide_show(self):
        inpb = self.driver.find_element(By.ID, "displayed-text")
        print(inpb.is_displayed())
        time.sleep(2)
        # hide
        self.driver.find_element(By.ID, "hide-textbox").click()
        print(inpb.is_displayed())
        time.sleep(2)
        # show
        self.driver.find_element(By.ID, "show-textbox").click()
        print(inpb.is_displayed())
        time.sleep(2)

    def scroll_into_view(self):
        ele = self.driver.find_element(By.ID, "displayed-text")
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)

    def scroll_into_view2(self, ele):
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)

    def dynamic_dropdown(self):
        self.driver.find_element(By.ID, "autocomplete").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ui-menu-item")))
            ele = self.driver.find_elements(By.CLASS_NAME, "ui-menu-item")
            for e in ele:
                txt = e.text
                if txt == 'Indonesia':
                    e.click()
                    v = self.driver.find_element(By.ID, "autocomplete").get_attribute("value")
                    time.sleep(3)
                    print(v)
                    if v == 'Indonesia':
                        print("success")
                    else:
                        print("failed")
                    break

        except Exception as e:
            print(e)

    def new_tab(self):
        print(self.driver.title)
        # self.driver.find_element(By.ID, "opentab").click()
        # print(self.driver.title)
        # time.sleep(2)
        # wh = self.driver.window_handles
        # print(wh)
        # self.driver.switch_to.window(wh[1])
        # print(self.driver.title)
        # time.sleep(2)
        # self.driver.get("https://formy-project.herokuapp.com/")
        # print(self.driver.title)
        # time.sleep(2)
        # self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
        cwh = self.driver.current_window_handle
        self.driver.execute_script("window.open("");")
        wh = self.driver.window_handles
        print(wh)
        # self.driver.switch_to.window(wh[1])
        self.driver.switch_to.window(window_name=wh[1])
        self.driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")
        print(self.driver.title)
        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(cwh)
        print(self.driver.title)
        time.sleep(2)
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        time.sleep(2)

    def mouse_hover(self):
        ele = self.driver.find_element(By.ID, "mousehover")
        self.scroll_into_view2(ele)
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

        action.click(self.driver.find_element(By.LINK_TEXT, "Top")).perform()
        time.sleep(3)

    def mouse_hover_reuse(self, ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
        time.sleep(1)
        return action

    def frame(self):
        print(self.driver.title)
        frame = self.driver.find_element(By.ID, "courses-iframe")
        self.driver.switch_to.frame(frame)
        more = self.driver.find_element(By.LINK_TEXT, "More")
        self.scroll_into_view2(more)
        self.mouse_hover_reuse(more)
        time.sleep(2)

    def table_1(self):
        table = self.driver.find_element(By.XPATH, "//table[@id='product' and @name='courses']/tbody")
        self.scroll_into_view2(table)
        rows = table.find_elements(By.XPATH, "tr")
        col = table.find_elements(By.XPATH, "tr/td[1]")
        print(len(rows))
        print(len(col))
        # for row in rows:
        #     print(row.text)
        instructor_previous = ''
        amt = 0
        course = []
        for i in range(2, len(rows)):
            instructor = rows[i].find_element(By.XPATH, "td[1]").text
            if i == 2:
                instructor_previous = instructor
            if instructor == instructor_previous:
                instructor_previous = instructor
                amt += int(rows[i].find_element(By.XPATH, "td[3]").text)
                course.append(rows[i].find_element(By.XPATH, "td[2]").text)
        print(f'{instructor_previous}: {amt}\n{course}')

    def table_2(self):
        table = self.driver.find_element(By.XPATH, "//div[@class='tableFixHead']//tbody")
        self.scroll_into_view2(table)
        rows = table.find_elements(By.XPATH, "tr")
        cols = table.find_elements(By.XPATH, "tr/td[1]")
        print(len(rows))
        print(len(cols))

        profession = "Engineer"
        profession_s = 0
        total_s = 0
        for row in rows:
            prof = row.find_element(By.XPATH, "td[2]").text
            if prof == profession:
                name = row.find_element(By.XPATH, "td[1]").text
                city = row.find_element(By.XPATH, "td[3]").text
                amt = row.find_element(By.XPATH, "td[4]").text
                print(name, prof, city, amt)
                profession_s += int(amt)

            total_s += int(row.find_element(By.XPATH, "td[4]").text)

        print(f'{profession}: {profession_s}')
        print()
        given_total = self.driver.find_element(By.XPATH, "//div[@class='totalAmount']").text
        given_total = given_total.split(":")[1].strip()
        if int(given_total) == total_s:
            assert int(given_total) == total_s
            print("Yes")
            print(given_total)
            print(total_s)

    def broken_link(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            link_name = link.text
            url = link.get_attribute("href")
            # print(link_name, url)
            try:
                res = requests.head(url)
                if res.status_code != 200:
                    print(f'{link_name}, is broken, {url}, {res.status_code}')
            except Exception as e:
                print(e)

    def broken_link2(self):
        from urllib.request import urlopen
        from urllib.error import HTTPError, URLError
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            url = link.get_attribute("href")
            try:
                urlopen(url)
            except (HTTPError, URLError):
                print(f"Broken link: {url}")

    def broken_image(self):
        from urllib.request import urlopen
        from urllib.error import HTTPError, URLError
        self.driver.get("https://the-internet.herokuapp.com/broken_images")
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for image in images:
            src = image.get_attribute("src")
            try:
                urlopen(src)
            except (HTTPError, URLError):
                print(f"Broken image: {src}")


if __name__ == '__main__':
    d = Demo()
    d.broken_link2()
