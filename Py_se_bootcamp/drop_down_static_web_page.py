from  selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

def static_web_page():
    driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
    driver.get("https://www.facebook.com")
    sleep(2)
    driver.maximize_window()
    print(driver.title)
    sleep(3)
    day_locator=driver.find_element_by_id("day")
    Select_day=Select(day_locator)
    Select_day.select_by_value("7")
    sleep(3)
    Month_locator=driver.find_element_by_id("month")
    Select_month=Select(Month_locator)
    Select_month.select_by_index("2")
    sleep(3)
    year_locator=driver.find_element_by_id("year")
    Select_year=Select(year_locator)
    Select_year.select_by_value("1999")
    sleep(3)
    custom_loc=driver.find_element_by_xpath("//span[@class='_5k_2 _5dba'][3]")
    custom_loc.click()
    sleep(3)
    pronoun=driver.find_element_by_xpath("//select[@class='_7-16 _5dba']")
    pronoun.click()
    Select_pronoun=Select(pronoun)
    Select_pronoun.select_by_index("1")
    print(pronoun.text)
    sleep(3)
    pronoun_expected_list=['She: "Wish her a happy birthday!"',
                           'He: "Wish him a happy birthday!"',
                           'They: "Wish them a happy birthday!"']
    sleep(3)
    Select_your_pronoun=driver.find_elements_by_xpath("//div/select/option")
    print("lenth_of_Select your pronoun: ",len(Select_your_pronoun))
    for name in Select_your_pronoun:

            print("   {}:".format(name.text))

    sleep(3)




    driver.close()
    driver.quit()
static_web_page()