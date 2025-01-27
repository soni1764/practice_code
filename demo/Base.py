import inspect
import logging

import pytest

from demo.conftest import driver_


# @pytest.mark.usefixtures('testdata')
@pytest.mark.usefixtures('driver_')
class Base:

    # driver = None
    #
    # @pytest.fixture(autouse=True)
    # def setup_base(self, driver_):
    #     self.driver = driver_

    def get_logger(self):
        # logger = logging.getLogger(__name__)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("test.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        # logger.debug("debug")
        # logger.info("info")
        # logger.warning("warning")
        # logger.error("error")
        # logger.critical("critical")
        return logger