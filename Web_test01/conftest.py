from time import sleep

import pytest


#@pytest.fixture(scope='module')
# from pytestfunctions.arithmetic_class import ArithmeticClass
from selenium import webdriver


@pytest.fixture(scope='class')
def oneTimeSetUp(request):
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.explorechoice.org/")
    sleep(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    print('drive close')
    driver.close()
    print('driver quit')
    driver.quit()