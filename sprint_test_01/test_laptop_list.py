from selenium import webdriver
from time import sleep
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_laptop_list:

    @pytest.fixture()
    def setup(self):
       self.driver.save_scre


    def test_laptiop(self,setup):

        click_on_laptop=self.driver.find_element_by_xpath("(//a[@class='list-group-item'])[3]")
        click_on_laptop.click()
        print("click on laptop")
        sleep(5)
    def test_homepage_title(self,setup):
        print('Getting homepage title')
        page_title = self.driver.title
        print('Comparing title')
        assert page_title=='explorechoice.org'

