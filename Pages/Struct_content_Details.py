import time
from selenium.webdriver.support.select import Select
class Struct_Content_Details():


    def __init__(self,driver):
        self.driver=driver
        self.Valuation_selection_xpath='//*[@id="HomeShield_SelectedValueType"]'
        self.Struct_value_textbox_id='StructureValue'
        self.content_value_textbox_id='ContentValue'
        self.area_textbox_id='HomeShield_Area'
        self.age_of_building_selection_id='drop'
        self.floortype_selection_id='dropSelectPropertyType'
        self.prop_impact_slider_xpath='//*[@id="frm_StructCont_HS"]/div[2]/div[2]/p[2]'
        self.security_24X7_slider_xpath='//*[@id="frm_StructCont_HS"]/div[3]/div[2]/div/div/p[2]/label/span'
        self.intercome_slider_xpath ='//*[@id="frm_StructCont_HS"]/div[3]/div[3]/div/div/p[2]/label/span'
        self.salaried_slider_xpath='//*[@id="frm_StructCont_HS"]/div[4]/div[1]/div/p/label/span'
        self.next_button_xpath='//*[@id="frm_StructCont_HS"]/div[4]/div[2]/a'
        self.next_button2_xpath='//*[@class="customize-btn sec-btn btn_StructCont_HS"]'
        self.next_button1_xpath='//*[@id="frm_StructCont_HS"]/div[3]/div[2]/a'
        self.name_textbox_id='FullName'
        self.email_textbox_id='Email'
        self.mobile_textbox_id='MobileNo'
        self.declaration_checkbox_xpath='//*[@id="ViewQuoteCondition"]'
        self.viewquote_button_xpath='//*[@id="modal1"]/div/div/div/div[2]/button'



    def Select_Valuation(self,value):
        Selection=Select(self.driver.find_element_by_xpath(self.Valuation_selection_xpath))
        Selection.select_by_value('28')
        self.driver.find_element_by_id(self.Struct_value_textbox_id).send_keys(value)

    def Select_Struct_content_Valuation(self,value):
        self.driver.find_element_by_id(self.content_value_textbox_id).send_keys(value)

    def Select_Tenanat_Valuation(self,value):
        self.driver.find_element_by_id(self.content_value_textbox_id).send_keys(value)


    def Builtup_Area(self,area):
        self.driver.find_element_by_id(self.area_textbox_id).clear()
        self.driver.find_element_by_id(self.area_textbox_id).send_keys(area)
        Selection_Age=Select(self.driver.find_element_by_id(self.age_of_building_selection_id))
        Selection_Age.select_by_value('12')

    def Select_AgeofProp_PropType(self):
        Selection_Floor = Select(self.driver.find_element_by_id(self.floortype_selection_id))
        Selection_Floor.select_by_value('1')

    def Select_Security_Measures(self):
        self.driver.find_element_by_xpath(self.security_24X7_slider_xpath).click()
        self.driver.find_element_by_xpath(self.intercome_slider_xpath).click()
        self.driver.find_element_by_xpath(self.salaried_slider_xpath).click()

    def Click_Next_Button(self):
        self.driver.find_element_by_xpath(self.next_button2_xpath).click()
    def Click_Next_Button_Tenant(self):
        self.driver.find_element_by_xpath(self.next_button1_xpath).click()

    def Entering_Basic_Details(self,name,email,mobile):
        self.driver.find_element_by_id(self.name_textbox_id).send_keys(name)
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)
        self.driver.find_element_by_id(self.mobile_textbox_id).send_keys(mobile)
        checkbox=self.driver.find_element_by_xpath(self.declaration_checkbox_xpath)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.find_element_by_xpath(self.viewquote_button_xpath).click()
