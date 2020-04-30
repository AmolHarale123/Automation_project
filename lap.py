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
sleep(3)
title_of_product=driver.find_element_by_xpath("//a[text()='Sony vaio i5']")
print("title of product:",title_of_product.text)
sleep(4)
prise_of_product=driver.find_element_by_xpath("(//h5[text()='$790'])[1]")
print(prise_of_product.text)
sleep(3)
click_on_select_product=driver.find_element_by_xpath("(//div[@class='card h-100'])[1]")
click_on_select_product.click()
sleep(5)
prise_of_product=driver.find_element_by_xpath("//h3[@class='price-container']")
print(prise_of_product.text)






driver.close()
driver.quit()