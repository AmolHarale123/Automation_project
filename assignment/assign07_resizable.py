from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains




def resizable():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://jqueryui.com/resizable/")
    sleep(2)
    driver.maximize_window()
    print(driver.title)

    sleep(4)
    driver.switch_to.frame(0)
    #click_resizable=driver.find_element_by_xpath("//a[text()='Resizable']")
   # click_resizable.click()
    sleep(3)
    action=ActionChains(driver)
    resizable=driver.find_element_by_xpath("//div[@class='ui-widget-content ui-resizable']")

    action.drag_and_drop_by_offset(resizable,100,100).perform()
    sleep(5)




    driver.close()
    driver.quit()
resizable()