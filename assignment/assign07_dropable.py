from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def dropable():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://jqueryui.com/droppable/")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    action=ActionChains(driver)
    sleep(4)
    driver.switch_to.frame(0)
    source=driver.find_element_by_id("draggable")
    dropable=driver.find_element_by_id("droppable")
    action.click_and_hold(source).drag_and_drop(source,dropable).perform()
    sleep(5)




    driver.close()
    driver.quit()
dropable()