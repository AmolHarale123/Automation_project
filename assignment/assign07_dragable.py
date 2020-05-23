from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def dragable():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://jqueryui.com/droppable/")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    action=ActionChains(driver)
    sleep(4)
    driver.switch_to.frame(0)
    dragable=driver.find_element_by_xpath('//div[@id="draggable"]')
    action.click_and_hold(dragable).drag_and_drop_by_offset(dragable,150,50).perform()
    sleep(5)




    driver.close()
    driver.quit()
drag_drop()