from selenium import webdriver
from time import sleep

def serach_box():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.flipkart.com")
    print(driver.title)
    sleep(3)
    driver.maximize_window()
    sleep(2)
    pop_upWindow=driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
    pop_upWindow.click()
    sleep(2)
    serach_box=driver.find_element_by_name("q")
    serach_box.send_keys("Delll laptop")
    sleep(2)
    search_icon = driver.find_element_by_xpath("//button[@type='submit']")
    search_icon.click()
    sleep(4)
    product_list=driver.find_element_by_xpath("//div[@class='_3O0U0u']//a[@class='_2cLu-l']")
    print(product_list.text)
    sleep(2)
    product_list=driver.find_elements_by_xpath("//div[@class='_3O0U0u']//a[@class='_2cLu-l']")
    print(len(product_list))
    sleep(4)
    for product in product_list:
        print(product.text)
    expected_product_list=["Dell 14 3000 Core i3 7th Gen - (4 GB/1 TB HDD/Linux) in...",
                           "Dell Inspiron 13 5000 Series Core i3 7th Gen - (4 GB/1 ...",
                            "Dell Vostro 3000 Core i3 8th Gen - (4 GB/1 TB HDD/Linux...",
                            "Dell Inspiron 5000 Core i5 8th Gen - (8 GB/1 TB HDD/512...",
                            "Dell 14 3000 Core i3 7th Gen - (4 GB/1 TB HDD/Windows 1..."]
    for i in range(0,len(expected_product_list)):
        if(product_list[i].text==expected_product_list[i]):
            print("product is in list {} ".format(product_list[i].text))
        else:
            print("product is not in list")

    #print(len(product_list))
    sleep(4)


    driver.close()
    driver.quit()
serach_box()
#//div[@class='_3O0U0u']//div[@class='_1vC4OE']