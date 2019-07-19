class home_insurance_homepage():


    def __init__(self,driver):
        self.driver=driver
        self.buynow_button_xpath='//button[text()=" Buy Now"]'

    def Click_on_Buy_Now(self):
        self.driver.find_element_by_xpath(self.buynow_button_xpath).click()
