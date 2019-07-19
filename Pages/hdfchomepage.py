class hdfchomepage():


    def __init__(self,driver):
        self.driver=driver
        self.homeinsurance_link_xpath='//*[@id="menu-slider-carousel"]/div/div[5]/a'


    def selecting_homeinsurance(self):
        self.driver.find_element_by_xpath(self.homeinsurance_link_xpath).click()
