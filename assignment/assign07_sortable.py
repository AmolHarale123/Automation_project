from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def sortable():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://jqueryui.com/sortable/")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    action=ActionChains(driver)
    sleep(4)
    driver.switch_to.frame(0)
    sortable_element=driver.find_elements_by_xpath("//li[@class='ui-state-default ui-sortable-handle']")

    print(len(sortable_element))
    #print("reverse order: " ,sortable_element.reverse())
    sortable_element.reverse()
    for i in sortable_element:

        print(i.text)





    sleep(5)



    driver.close()
    driver.quit()
sortable()


