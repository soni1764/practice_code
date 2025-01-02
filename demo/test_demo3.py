
import pytest

from demo.Base import Base
from tests.conftest import driver


# def test_first_program(setup):
#     print("hi")

# @pytest.mark.usefixtures('setup_at_method')
# @pytest.mark.usefixtures('setup_at_class')
# class TestDemo:
#
#     def test_first_program(self):
#         print("hi1111111111111")
#
#     def test_sec_program(self):
#         print("hi22222222222222")
#
#     def test_third_program(self):
#         print("hi33333333333333")
#
#     def test_fourth_program(self):
#         print("hi44444444444444")


# @pytest.mark.usefixtures('payload')
# class TestDemo2:
#
#     def test_first_program(self, payload):
#         print("hi1111111111111")
#         print(payload)
#
#     def test_sec_program(self, payload):
#         print("hi22222222222222")
#         print(payload)
#
#     def test_third_program(self, payload):
#         print("hi33333333333333")
#         print(payload)
#
#     def test_fourth_program(self, payload):
#         print("hi44444444444444")
#         print(payload)



# def test_first_program(cross_browser):
#     print("hi1111111111111")
#     print(cross_browser)



class TestDemo2(Base):

    # def test_first_program(self):
    #     print("hi1111111111111")
    #     logger = self.get_logger()
    #     logger.info("running first test")

    def test_get_title(self):
        logger = self.get_logger()
        logger.info("running first test")
        self.driver.get("https://www.google.com/")
        logger.info(self.driver.title)
        assert self.driver.title == 'Google'

    # def test_data(self, testdata):
    #     print(testdata)

# def test_get_title(driver_2):
#     driver_2.get("https://www.google.com/")
#     assert driver_2.title == 'Google'




