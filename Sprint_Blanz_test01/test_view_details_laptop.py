from selenium import webdriver
from html_reports import reports
from time import sleep
import pytest



@pytest.mark.usefixtures("oneTimeSetUp")
class Test_view_details_laptop:


    def test_Namepage_title(self):
        print('Getting homepage title')
        page_title = self.driver.title
        sleep(3)
        self.driver.save_screenshot("../Screenshot/namepage.png")
        print("page_title: ", page_title)
        assert page_title=='STORE'
    def test_Details_of_laptop(self):

        click_on_laptop=self.driver.find_element_by_xpath("(//a[@class='list-group-item'])[3]")
        click_on_laptop.click()
        sleep(3)
        title_of_product=self.driver.find_element_by_xpath("//a[text()='Sony vaio i5']")
        print("title of product:",title_of_product.text)
        sleep(4)

        click_on_select_product=self.driver.find_element_by_xpath("(//div[@class='card h-100'])[1]")
        click_on_select_product.click()
        sleep(3)

        prise_of_product=self.driver.find_element_by_xpath("//h3[@class='price-container']")
        print("prise of product: ", prise_of_product.text)
        self.driver.save_screenshot("../Screenshot/details_of_product.png")
        sleep(2)





        assert prise_of_product.text=='$790 *includes tax'

