import pytest
from selenium import webdriver

import data


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()  # запуск Chrome
    chrome_driver.get(data.DRIVER)  # запуск приложения Stellar Burgers

    yield chrome_driver

    chrome_driver.quit()