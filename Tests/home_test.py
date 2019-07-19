import pytest
from Pages.hdfchomepage import hdfchomepage
from Pages.home_insurance_homepage import home_insurance_homepage
from Pages.homeinsurance_coverpage import home_insurance_coverage
from Pages.Struct_content_Details import Struct_Content_Details
from Pages.Customize_Quote import Customize_Quote
from Pages.Fill_Details import Fill_Details
from Utils import util as utils
import time



@pytest.mark.usefixtures('Setup')
class Test_Home_selc():

    # Home insurance quote for structure
    def test_owner_quote_structure(self):

        # Calling Driver
        driver=self.driver

        # Launching HDFC ERGO Home Page
        driver.get(utils.url)

        # Selecting Home Insurance
        Hdfchome=hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()

        # Selecting Buy Now Button
        Home_insur=home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()

        # Switching from Current window to Quote Window
        driver.switch_to.window(driver.window_handles[1])

        # Selecting Insurance type
        coverpage=home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()

        # Selecting  Structure Type and etc...
        Struct_Content=Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name,utils.email,utils.mobile)




    # Renter Quote for Content value
    def test_tenant_quote_content(self):
        driver=self.driver
        driver.get(utils.url)
        Hdfchome=hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur=home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage=home_insurance_coverage(driver)
        coverpage.Selection_Tenant()
        #coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()
        Struct_Content=Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Tenanat_Valuation(utils.value)
        #Struct_Content.Builtup_Area(utils.area)
        #Struct_Content.Select_AgeofProp_PropType()
        #Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button_Tenant()
        Struct_Content.Entering_Basic_Details(utils.name,utils.email,utils.mobile)

    # Home insurance quote for structure and Content(Both) value
    def test_owner_quote_structure_content(self):
        driver=self.driver
        driver.get(utils.url)
        Hdfchome=hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur=home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage=home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_content_type()
        coverpage.Click_On_Continue()
        Struct_Content=Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        #Struct_Content.Select_Security_Measures()
        Struct_Content.Select_Tenanat_Valuation('100000')
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name,utils.email,utils.mobile)

    # Additional coverages to Home insurance quote for structure
    def test_add_additional_coverages(self):
        driver = self.driver
        driver.get(utils.url)
        Hdfchome = hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur = home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage = home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()
        Struct_Content = Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name, utils.email, utils.mobile)
        time.sleep(4)
        CustomizeQuote=Customize_Quote(driver)
        CustomizeQuote.Select_Additonal_Coverage(utils.bicycle_coverage)
        CustomizeQuote.Select_Quote()


    # Add Co-owner to Home insurance quote for structure
    def test_add_coowner(self):
        driver = self.driver
        driver.get(utils.url)
        Hdfchome = hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur = home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage = home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()
        Struct_Content = Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name, utils.email, utils.mobile)
        time.sleep(4)
        CustomizeQuote = Customize_Quote(driver)
        time.sleep(5)
        #CustomizeQuote.Select_Additonal_Coverage(utils.bicycle_coverage)
        CustomizeQuote.Select_Quote()
        filldetails=Fill_Details(driver)
        time.sleep(3)
        filldetails.Select_Coowner(utils.coowner)
        filldetails.Select_Address(utils.dob,utils.pincode,utils.h_no,utils.street)


    # Correspondence address different
    def test_correspondance_address(self):
        driver = self.driver
        driver.get(utils.url)
        Hdfchome = hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur = home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage = home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()
        Struct_Content = Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name, utils.email, utils.mobile)
        time.sleep(4)
        CustomizeQuote = Customize_Quote(driver)
        time.sleep(5)
        # CustomizeQuote.Select_Additonal_Coverage(utils.bicycle_coverage)
        CustomizeQuote.Select_Quote()
        filldetails = Fill_Details(driver)
        time.sleep(3)
        filldetails.Select_Coowner(utils.coowner)
        filldetails.Select_Address(utils.dob, utils.pincode, utils.h_no, utils.street)
        filldetails.Select_Correspondance_Address(utils.cpincode,utils.chno,utils.cstreet)
        filldetails.Select_Next_Button()

    #Add financier details
    def test_add_fianacier(self):
        driver = self.driver
        driver.get(utils.url)
        Hdfchome = hdfchomepage(driver)
        Hdfchome.selecting_homeinsurance()
        Home_insur = home_insurance_homepage(driver)
        Home_insur.Click_on_Buy_Now()
        driver.switch_to.window(driver.window_handles[1])
        coverpage = home_insurance_coverage(driver)
        coverpage.Selection_type()
        coverpage.Selcetion_struct_type()
        coverpage.Click_On_Continue()
        Struct_Content = Struct_Content_Details(driver)
        time.sleep(5)
        Struct_Content.Select_Valuation(utils.value)
        Struct_Content.Builtup_Area(utils.area)
        Struct_Content.Select_AgeofProp_PropType()
        #Struct_Content.Select_Security_Measures()
        Struct_Content.Click_Next_Button()
        Struct_Content.Entering_Basic_Details(utils.name, utils.email, utils.mobile)
        time.sleep(4)
        CustomizeQuote = Customize_Quote(driver)
        time.sleep(5)
        # CustomizeQuote.Select_Additonal_Coverage(utils.bicycle_coverage)
        CustomizeQuote.Select_Quote()
        filldetails = Fill_Details(driver)
        time.sleep(3)
        #filldetails.Select_Coowner(utils.coowner)
        filldetails.Select_Address(utils.dob, utils.pincode, utils.h_no, utils.street)
        #filldetails.Select_Correspondance_Address(utils.cpincode,utils.chno,utils.cstreet)
        filldetails.Select_fiancier(utils.financier)
        filldetails.Select_Next_Button()