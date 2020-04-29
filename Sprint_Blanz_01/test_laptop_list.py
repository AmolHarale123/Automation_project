from selenium import webdriver
from html_reports import reports
from time import sleep
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_laptop_list:


    def test_Namepage_title(self):
        print('Getting homepage title')
        page_title = self.driver.title
        sleep(3)
        self.driver.save_screenshot("../Screenshot/namepage.png")
        print("page_title: ", page_title)
        assert page_title=='STORE'
    def test_laptiop(self):

        click_on_laptop=self.driver.find_element_by_xpath("(//a[@class='list-group-item'])[3]")
        click_on_laptop.click()
        sleep(4)
        self.driver.save_screenshot("../Screenshot/list_laptop.png")
        sleep(3)
        laptop_list=self.driver.find_element_by_xpath('//div/h4[@class="card-title"]')
        print("laptop_list: ", laptop_list.text)

        assert laptop_list.text=="Sony vaio i5"
        sleep(5)

