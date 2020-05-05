from selenium import webdriver
from time import sleep



print("------------------------------------------------product_prise_low_to_high-----------------------------------------------------")

def product_prise_low_to_high():
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
        sleep(3)
        prise_low_to_high=driver.find_element_by_xpath("//div[text()='Price -- Low to High']")
        prise_low_to_high.click()
        sleep(4)
        product_list=driver.find_element_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
        print(product_list.text)
        sleep(2)
        product_prise_list=driver.find_elements_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")#product_prise_list locator
        print( "lenght of product_prise_low_to_high: ", len(product_prise_list))#lenght of list prise
        sleep(4)
        for product in product_prise_list:
            print(product.text)

        expected_product_prise_list=["₹21,990","₹22,999","₹₹23,490","₹24,000","₹25,490","₹25,990","₹26,990","₹42,990","₹50,990","₹27,990"]



        for i in range(0,len(expected_product_prise_list)):
            if(product_prise_list[i].text==expected_product_prise_list[i]):
                print("product of prise is in list {} ".format(product_prise_list[i].text))
            else:
                print("product is not in list")
        sleep(4)

        print("------------------------------------------------product_prise_high_to_low------------------------------------------------------")
def product_prise_high_to_low():

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
    sleep(3)
    prise_high_to_low=driver.find_element_by_xpath("//div[text()='Price -- High to Low']")
    prise_high_to_low.click()
    sleep(4)
    product_prise_high_to_low=driver.find_element_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
    print("product_prise: ", product_prise_high_to_low.text)
    sleep(3)
    product_prise_high_to_low=driver.find_elements_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
    print("lenght of product_prise_high_to_low: ", len(product_prise_high_to_low))
    sleep(3)
    print("product_prise_high_to_low :")
    for product_prise in product_prise_high_to_low:
        print(product_prise.text)
    #expected_product_prise_list locator
    expected_product_prise_list=["₹2,48,990","₹1,76,407","₹1,65,000","₹1,51,575","₹1,37,103",
                                "₹1,13,000","₹1,29,990","₹1,24,000","₹1,20,000","₹1,15,185"]
    for i in range(0,len(expected_product_prise_list)):
        if(product_prise_high_to_low[i].text==expected_product_prise_list[i]):

            print("product_prise is in list {} ".format(product_prise_high_to_low[i].text))
        else:
            print("product_prise is in list")
    sleep(4)



    driver.close()
    driver.quit()
product_prise_low_to_high()
product_prise_high_to_low()
