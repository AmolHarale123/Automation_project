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
    #pop_up_window close locator
    pop_up_window=driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
    pop_up_window.click()#pop_up_window  close
    sleep(3)
    action=ActionChains(driver)
    Electronic=driver.find_element_by_xpath("//span[text()='Electronics']")
    action.move_to_element(Electronic).perform()
    sleep(2)
    real_me=driver.find_element_by_xpath("//a[text()='Realme']")
    action.move_to_element(real_me).click().perform()
    sleep(5)
    print("====================Detail of Realme_5i Wtih Ratings & Reviews==================== ")

    #Realme 5i, realmi_phone locatior
    Realme_5i=driver.find_element_by_xpath("(//div[@class='col col-7-12'])[1]")
    print( Realme_5i.text)

    sleep(5)



    driver.close()
    driver.quit()
dynamic_web_page()