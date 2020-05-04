from selenium import webdriver
import time


def verify_search_functionality(search_text):
    # ARRANGE

    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(4)

    ## ACTION
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click();

    search_box = driver.find_element_by_name("q")  # Find the location of search box
    # search_box.send_keys("Macbook pro")   # to enter text we have to use send_keys()
    search_box.send_keys(search_text)

    # Finding xpath using contains(attribute, textwithinattributevalue)
    search_icon = driver.find_element_by_xpath("//button[@type='submit']")
    search_icon.click()

    time.sleep(5)

    product_list = driver.find_element_by_xpath("//div[@class='_1HmYoV _35HD7C'][2]//div[@class='_3wU53n']")
    print(product_list.text)

    products_list = driver.find_elements_by_xpath("//div[@class='_1HmYoV _35HD7C'][2]//div[@class='_3wU53n']")
    print(len(products_list))
    for product in products_list:
        print(product.text)


    expected_product_lists = [
        'Apple MacBook Pro Core i5 8th Gen - (8 GB/256 GB SSD/Mac OS Mojave) MV962HN', 'Apple MacBook Pro Core i5 8th Gen - (8 GB/512 GB SSD/Mac OS Mojave) MV972HN',
        'Apple MacBook Pro Core i5 8th Gen - (8 GB/128 GB SSD/Mac OS Mojave) MUHN2HN/A'
    ]

    for i in range(0, len(expected_product_lists)):
        if(products_list[i].text == expected_product_lists[i]):
            print("The prouct name is valid")
        else:
            print("The product name is invalid")



verify_search_functionality("Macbook pro")