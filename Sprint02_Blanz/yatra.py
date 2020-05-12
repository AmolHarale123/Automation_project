from  selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

def hotel_discounts_section():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.yatra.com/hotels")
    sleep(2)
    driver.maximize_window()
    print(driver.title)

    Select_city=driver.find_element_by_xpath("//input[@type='text']")
    Select_city=Select(Select_city)
    Select_city.select_by_visible_text("New Delhi,Delhi,India")
    Select_city.send_keys("New Delhi")
    Select_city.click()



    sleep(7)



    driver.close()
    driver.quit()
hotel_discounts_section()