from  selenium import webdriver
from time import sleep



def hotel_discounts_section():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.yatra.com/hotels")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    sleep(4)

    Search_hotels=driver.find_element_by_xpath('//input[@id="BE_hotel_htsearch_btn"]')
    Search_hotels.click()
    sleep(5)

    #hotails_detail=driver.find_element_by_xpath("(//div[@class='result-details-wrapper full'])[1]")
    #print(hotails_detail.text)

    sleep(4)
    name_of_hotels=driver.find_elements_by_xpath("//a[@class='under-link ng-binding']")
    print("Number_of_Hotels :" ,len(name_of_hotels))
    print("Name of Hotels lis: ")
    for Name in name_of_hotels:
        print("Name_of_Hotel: ",Name.text)
    sleep(5)

    dicount_offer=driver.find_elements_by_xpath("//span[@class='color-base ng-binding']")
    print( len(dicount_offer))
    print("Some Discount And Offer are: ")
    for discount in dicount_offer:
        print(discount.text)









    driver.close()
    driver.quit()
hotel_discounts_section()


