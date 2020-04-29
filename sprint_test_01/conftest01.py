from time import sleep
from selenium import webdriver

import pytest



@pytest.fixture(scope='class')
def oneTimeSetUp():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.demoblaze.com")
    sleep(4)
    driver.maximize_window()
    #request.cls.driver = driver
   # yield driver
    #print('drive close')
    #driver.close()
    #print('driver quit')
    #driver.quit()