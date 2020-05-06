import pytest
from time import sleep


@pytest.mark.usefixtures("one_Time_SetUp")
class Test_flipkart_product:
    @pytest.fixture()
    def test_setUp(self):
        print('Getting homepage title')
        page_title = self.driver.title
        sleep(3)
        self.driver.save_screenshot("../Screenshot/flipkart_namepage.png")
        sleep(2)
        print("page_title: ", page_title)
        sleep(2)
        self.driver.save_screenshot("../Screenshot/flipkartProductName.png")
        search_icon = self.driver.find_element_by_xpath("//button[@type='submit']")
        search_icon.click()
        sleep(4)

    def test_product_prise_low_to_high(self,test_setUp):


        prise_low_to_high=self.driver.find_element_by_xpath("//div[text()='Price -- Low to High']")
        prise_low_to_high.click()
        sleep(2)
        self.driver.save_screenshot("../Screenshot/flipkartPrisePage01.png")
        sleep(4)
        product_list=self.driver.find_element_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
        print(product_list.text)
        sleep(2)
        product_prise_list=self.driver.find_elements_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")#product_prise_list locator
        print( "lenght of product_prise_low_to_high: ", len(product_prise_list))#lenght of list prise
        sleep(4)
        for product in product_prise_list:
            print(product.text)

        expected_product_prise_list=["₹21,990","₹22,999","₹₹23,490","₹24,000","₹25,490","₹25,990","₹26,990","₹42,990","₹50,990","₹27,990"]



        for i in range(0,len(expected_product_prise_list)):
            if(product_prise_list[i].text==expected_product_prise_list[i]):
                print("product of prise is in list {} ".format(product_prise_list[i].text))
            else:
                print("product is not in list")
        sleep(4)

        assert product_prise_list[i].text==expected_product_prise_list[i]


    def test_product_prise_high_to_low(self,test_setUp):


        prise_high_to_low=self.driver.find_element_by_xpath("//div[text()='Price -- High to Low']")
        prise_high_to_low.click()
        sleep(2)
        self.driver.save_screenshot("../Screenshot/flipkartPrisePage02.png")
        sleep(4)
        product_prise_high_to_low=self.driver.find_element_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
        print("product_prise: ", product_prise_high_to_low.text)
        sleep(3)
        product_prise_high_to_low=self.driver.find_elements_by_xpath("//div[@class='_3O0U0u']//div[@class='_1vC4OE']")
        print("lenght of product_prise_high_to_low: ", len(product_prise_high_to_low))
        sleep(3)
        print("product_prise_high_to_low :")
        for product_prise in product_prise_high_to_low:
            print(product_prise.text)
        #expected_product_prise_list locator
        expected_product_prise_list=["₹2,48,990","₹1,76,407","₹1,65,000","₹1,51,575","₹1,37,103",
                                     "₹1,13,000","₹1,29,990","₹1,24,000","₹1,20,000","₹1,15,185"]
        for i in range(0,len(expected_product_prise_list)):
            if(product_prise_high_to_low[i].text==expected_product_prise_list[i]):

                print("product_prise is in list {} ".format(product_prise_high_to_low[i].text))
            else:
                print("product_prise is not in list")
        sleep(4)
        assert product_prise_high_to_low[0].text==expected_product_prise_list[0]
