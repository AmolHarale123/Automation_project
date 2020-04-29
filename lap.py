from selenium import webdriver
from time import sleep



driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://www.demoblaze.com")
print(driver.title)
sleep(4)
driver.maximize_window()
sleep(3)

click_on_laptop=driver.find_element_by_xpath("(//a[@class='list-group-item'])[3]")
click_on_laptop.click()
sleep(4)
laptop_list=driver.find_element_by_xpath('//div/h4[@class="card-title"]')
sleep(3)
print(laptop_list.text)






driver.close()
driver.quit()