import time
class home_insurance_coverage():


    def __init__(self,driver):
        self.driver=driver
        self.type_dropdown_xpath='//*[@class="pol-holder-list"]'
        self.ownership_selection_id='7'
        self.tenant_selection_id='8'
        self.covertype_dropdown_id='RiskCoverSpan'
        self.structure_selection_xpath='//*[@id="RiskCoverList"]/div[1]/div/label'
        self.structure_selection3_xpath='//*[@id="RiskCoverList"]/div[3]/div/label'
        self.struct_content_selection_xpath='//*[@id="RiskCoverList"]/div[2]/div/label'
        self.continue_button_xpath='//*[@id="car-homepage"]/div/div/div/div[2]/div/div/button'



    def Selection_type(self):
        self.driver.find_element_by_xpath(self.type_dropdown_xpath).click()
        self.driver.find_element_by_id(self.ownership_selection_id).click()

    def Selection_Tenant(self):
        self.driver.find_element_by_xpath(self.type_dropdown_xpath).click()
        self.driver.find_element_by_id(self.tenant_selection_id).click()

    def Selcetion_struct_type(self):
        self.driver.find_element_by_id(self.covertype_dropdown_id).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.structure_selection_xpath).click()

    def Selcetion_struct_content_type(self):
        self.driver.find_element_by_id(self.covertype_dropdown_id).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(self.structure_selection3_xpath).click()

    def Click_On_Continue(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()