from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.action_chains import ActionChains




def verify_mobiles_details():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    sleep(4)
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    actions = ActionChains(driver)
    electronics = driver.find_element_by_xpath("//span[text()='Electronics']")
    actions.move_to_element(electronics).click().perform()
    sleep(3)
    samsung_click = driver.find_element_by_xpath("(//a[text()='Samsung'])[1]")
    actions.move_to_element(samsung_click).click().perform()
    sleep(5)
    # actions.move_to_element(samsung_click).perform()
    # actions.click().perform()
      # web elements list of all product
    samsund_mob=driver.find_elements_by_xpath('//div[@class="_3liAhj _2Vsm67"]')
    sleep(5)
    print("lenth of samsund_mob:", len(samsund_mob))

    for samsung in samsund_mob[0:4]:
        print("list of mobile:",samsung.text)


    sleep(5)


verify_mobiles_details()






