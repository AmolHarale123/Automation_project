from time import sleep
from selenium import webdriver

import pytest


@pytest.fixture(scope='class')
def oneTimeSetUp(request):
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.yatra.com/hotels")
    sleep(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    #print('drive close')
    driver.close()
    #print('driver quit')
    driver.quit()