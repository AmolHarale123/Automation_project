from time import sleep
from selenium import webdriver

import pytest


@pytest.fixture(scope='class')
def one_Time_SetUp(request):
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.yatra.com/hotels")
    sleep(4)
    driver.maximize_window()
    sleep(2)
    request.cls.driver = driver

    yield driver
    #print('drive close')
    driver.close()
    #print('driver quit')
    driver.quit()