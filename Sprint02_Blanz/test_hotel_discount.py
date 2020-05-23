from time import sleep
import pytest

@pytest.mark.usefixtures("one_Time_SetUp")
class Test_hotel_discounts:



    def test_hotel_discounts_section(self):


        Search_hotels=self.driver.find_element_by_xpath('//input[@id="BE_hotel_htsearch_btn"]')
        Search_hotels.click()
        sleep(5)
        self.driver.save_screenshot("../Sprint02_Blanz/hotel_discount.png")
        print("=========================================hotails_detail====================================================")
        hotails_detail=self.driver.find_elements_by_xpath("//div[@class='result-details-wrapper full']")
        sleep(4)
        print("lenth of hoteil details list: ", len(hotails_detail))
        for hotels in hotails_detail:
            print(hotels.text)
            print("------------------------------------------------------------------------------------------------")

        assert len(hotails_detail)==30


