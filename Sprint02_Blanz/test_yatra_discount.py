from  selenium import webdriver
from time import sleep
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class testHotel_discounts:

    def test_name_of_city(self):
        print(self.driver.title)
        Select_city=self.driver.find_element_by_xpath("//input[@type='text']")
        Select_city.send_keys("New Delhi")
        Select_city.click()
        assert self.driver.title=="Hotels in India: Online Hotel Booking with Hot Deals & Discounts - Yatra.com"


    def test_hotel_discounts_section(self):


        Search_hotels=self.driver.find_element_by_xpath('//input[@id="BE_hotel_htsearch_btn"]')
        Search_hotels.click()
        sleep(5)
        print("=========================================hotails_detail====================================================")
        hotails_detail=self.driver.find_elements_by_xpath("//div[@class='result-details-wrapper full']")
        print("lenth of hoteil details list: ", len(hotails_detail))
        for hotels in hotails_detail:
            print(hotels.text)
            print("------------------------------------------------------------------------------------------------")
        #print(hotails_detail.text)

        assert len(hotails_detail)=="30"



