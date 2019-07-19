import time
from selenium.webdriver.support.select import Select
class Customize_Quote():

    def __init__(self,driver):
        self.driver=driver
        self.bicyclecover_link_xpath='//*[@id="AdditionalCovers"]/ul/li[2]/div/a'
        self.bicycle_sum_insured_textbox_id='BicycleSumInsured'
        self.terriosmcover_link_xpath='//*[@id="AdditionalCovers"]/ul/li[3]/div/a'
        self.quote_select_xpath='//*[@id="PlanSetup"]/div[2]/a'
        self.cong_popup_button_xpath='//*[@id="congratulations-popup"]/div/div/div/div/a'
        self.buynow_button_xpath='//a[@class="customize-btn sec-btn buy-btn btnBuyNow"]'

    def Select_Additonal_Coverage(self,bicyclev):
        time.sleep(5)
        bicycle=self.driver.find_element_by_xpath(self.bicyclecover_link_xpath)
        self.driver.execute_script("arguments[0].click();", bicycle)
        time.sleep(3)
        self.driver.find_element_by_id(self.bicycle_sum_insured_textbox_id).send_keys(bicyclev)
        self.driver.find_element_by_xpath(self.terriosmcover_link_xpath).click()

    def Select_Quote(self):
        time.sleep(5)
        element1 = self.driver.find_element_by_xpath(self.quote_select_xpath)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", element1)
        time.sleep(4)
        self.driver.find_element_by_xpath(self.cong_popup_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.buynow_button_xpath).click()