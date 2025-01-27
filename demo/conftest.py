import pytest
from selenium import webdriver


# scope of fixture - by default method level
@pytest.fixture()
def setup_at_method():
    print("I'll be executed first")
    yield
    print("I'll be executed last")


# scope of fixture - by default class level
@pytest.fixture(scope='class')
def setup_at_class():
    print("I'll be executed before class")
    yield
    print("I'll be executed after class")


# scope of fixture - by default module level
@pytest.fixture(scope='module')
def setup_at_module():
    print("I'll be executed before module")
    yield
    print("I'll be executed after module")


# scope of fixture - by default package level
@pytest.fixture(scope='package')
def setup_at_package():
    print("I'll be executed before package")
    yield
    print("I'll be executed after package")


# scope of fixture - by default session level
@pytest.fixture(scope='session')
def setup_at_session():
    print("I'll be executed before session")
    yield
    print("I'll be executed after session")


@pytest.fixture()
def payload():
    print("user data")
    return ["gourav", "soni", "xyz@gmail.com"]


@pytest.fixture(params=["chrome", "firefox", "ie", "safari"])
def cross_browser(request):
    return request.param


@pytest.fixture(scope="class")
def driver_(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(params=["chrome", "firefox", "ie"])
def driver_2(request):
    browser = request.param
    if browser == 'chrome':
        driver_instance = webdriver.Chrome()
    elif browser == 'firefox':
        driver_instance = webdriver.Firefox()
    elif browser == 'ie':
        driver_instance = webdriver.Ie()
    else:
        driver_instance = None
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(5)
    return driver_instance
    # driver_instance.quit()


@pytest.fixture(scope='class')
def testdata():
    return [1, 2, 3]
