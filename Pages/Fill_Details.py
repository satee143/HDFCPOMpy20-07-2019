import time
from selenium.webdriver.support.select import Select
class Fill_Details():

    def __init__(self,driver):
        self.driver=driver
        self.dob_textbox_id='DateOfBirth'
        self.coowner_span_xpath='//*[@id="CoOwnerDiv"]/div[1]/p[2]/label/span'
        self.coowner_name_textbox_id='CoOwnerName'
        self.pincode_textbox_id='InsuredPinCode'
        self.pincodex_select_xpath='//*[@id="insuredAddress"]/div[2]/div/ul/li/a/strong'
        self.houseno_textbox_id='InsuredAddress_HouseNo'
        self.street_textbox_id='InsureStreetSectorArea'
        self.correspondance_span_xpath='//*[@id="frm_InsuredCustDetail"]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/p[2]/label/span'
        self.correspondancepin_textbox_id='CPDPinCode'
        self.correspondancepin_select_xpath='//*[@id="correspondenceAddress"]/div[2]/div/ul/li/a/strong'
        self.correspondance_house_textbox_id='CorrespondenceAddress_HouseNo'
        self.correspondance_street_textbox_id='CPDStreetSectorArea'
        self.financier_span_xpath='//*[@id="LoanProviderDiv"]/div[1]/p[2]/label/span'
        self.loanprovider_textbox_id='LoanProvider'
        self.loanprov_select_xpath='//*[@id="LoanProviderDiv"]/div[2]/div/ul/li[1]/a'
        self.next_button_xpath='//*[@id="frm_InsuredCustDetail"]/div/div/div/div[2]/div/a'




    def Select_Coowner(self,coowner):
        self.driver.find_element_by_xpath(self.coowner_span_xpath).click()
        self.driver.find_element_by_id(self.coowner_name_textbox_id).send_keys(coowner)

    def Select_Address(self,dob,pincode,hno,street):
        self.driver.find_element_by_id(self.dob_textbox_id).send_keys(dob)
        self.driver.find_element_by_id(self.pincode_textbox_id).send_keys(pincode)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.pincodex_select_xpath).click()
        self.driver.find_element_by_id(self.houseno_textbox_id).send_keys(hno)
        self.driver.find_element_by_id(self.street_textbox_id).send_keys(street)

    def Select_Correspondance_Address(self,pincode,hno,street):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.correspondance_span_xpath).click()
        self.driver.find_element_by_id(self.correspondancepin_textbox_id).send_keys(pincode)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.correspondancepin_select_xpath).click()
        self.driver.find_element_by_id(self.correspondance_house_textbox_id).send_keys(hno)
        self.driver.find_element_by_id(self.correspondance_street_textbox_id).send_keys(street)

    def Select_fiancier(self,financier):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.financier_span_xpath).click()
        self.driver.find_element_by_id(self.loanprovider_textbox_id).send_keys(financier)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.loanprov_select_xpath).click()

    def Select_Next_Button(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()


