from page_objects.example_page import ExamplePage


def test_title(driver):
    driver.get("http://www.google.com")
    page = ExamplePage(driver)
    assert page.get_title() == "Google"


def test_About(driver):
    driver.get("https://www.google.com/")
    page = ExamplePage(driver)
    # assert "About" == page.get_about_text
