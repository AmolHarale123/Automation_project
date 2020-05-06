from time import sleep
from selenium import webdriver

import pytest


@pytest.fixture(scope='class')
def one_Time_SetUp(request):
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.flipkart.com")
    sleep(4)
    driver.maximize_window()
    pop_upWindow=driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
    pop_upWindow.click()
    sleep(3)
    serach_box=driver.find_element_by_name("q")
    serach_box.send_keys("Delll laptop")
    sleep(2)
    request.cls.driver = driver

    yield driver
    #print('drive close')
    driver.close()
    #print('driver quit')
    driver.quit()