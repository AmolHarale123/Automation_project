from selenium import webdriver
from html_reports import reports
import pytest
from selenium.webdriver.common.alert import Alert
from time import sleep




@pytest.mark.usefixtures("oneTimeSetUp")
class Test_add_to_cart:


    def test_Namepage_title(self):
        print('Getting homepage title')
        page_title = self.driver.title
        sleep(3)
        #self.driver.save_screenshot("../Screenshot/namepage.png")
        print("page_title: ", page_title)
        assert page_title=='STORE'


    def test_add_to_cart(self):
        alert=Alert(self.driver)

        click_on_laptop=self.driver.find_element_by_xpath("(//a[@class='list-group-item'])[3]")
        click_on_laptop.click()
        sleep(4)
        click_on_select_product=self.driver.find_element_by_xpath("(//div[@class='card h-100'])[1]")
        click_on_select_product.click()
        sleep(3)
        add_to_cart=self.driver.find_element_by_xpath("//a[text()='Add to cart']")
        add_to_cart.click()
        sleep(5)
        self.driver.save_screenshot("../Screenshot/Product added.png")
        sleep(3)
        self.driver.switch_to.alert
        alert_text=alert.text
        print("product_is_added: ", alert.text)
        alert.accept()
        assert alert_text=="Product added"












