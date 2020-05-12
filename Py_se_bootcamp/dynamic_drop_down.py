from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def dynamic_web_page():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.flipkart.com")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    sleep(4)
    pop_up_window=driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
    pop_up_window.click()
    sleep(3)
    action=ActionChains(driver)
    Electronic=driver.find_element_by_xpath("//span[text()='Electronics']")
    action.move_to_element(Electronic).perform()
    sleep(2)
    real_me=driver.find_element_by_xpath("//a[text()='Realme']")
    action.move_to_element(real_me).click().perform()
    sleep(5)
    #lenth of realmi_phone list locatior
    realme_phone=driver.find_elements_by_xpath("//div[@class='col col-7-12']")
    print("lenth of realme_phone: ", len(realme_phone))
    #realme_phone=driver.find_element_by_xpath("(//div[@class='_1-2Iqu row'])[1]")# All detail about real_me phone with prise of phone
    #print(realme_phone.text)
    sleep(5)
    for phone in realme_phone:
        print(phone.text)
        print("-----------------------------------------------------------------")



    driver.close()
    driver.quit()
dynamic_web_page()