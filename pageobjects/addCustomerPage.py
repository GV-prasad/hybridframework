import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class AddCustomer:
    lnkCustomer_menu_xpath = "(//a[@class='nav-link'])[21]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddCustomer_xpath = "//a[normalize-space()='Add new']"

    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_name = "DateOfBirth"
    txtCompany_id='Company'
    txtNewsLetter_xpath="//input[@class='k-input k-readonly']"
    sltitemStoreNAme_link_text="Your store name"
    sltitemTestStore_link_text="Test store 2"
    txtCompanyroles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[normalize-space()='Administrators']"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemRegistered_xpath = "//li[normalize-space()='Registered']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpManagerOfVendor_id = "VendorId"
    txtAdminComment_id = "AdminComment"
    btnSave_xpath = "(//i[@class='far fa-save'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,(self.lnkCustomer_menu_xpath)).click()

    def ClickOnCustomerMenuItem(self) :
        self.driver.find_element(By.XPATH,(self.lnkCustomer_menuitem_xpath)).click()

    def ClickOnAddCustomer(self):
        self.driver.find_element(By.XPATH,(self.btnAddCustomer_xpath)).click()

    def SetEmail(self, email):
        self.driver.find_element(By.ID,(self.txtEmail_id)).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.ID,(self.txtPassword_id)).send_keys(password)

    def SetFirstName(self, fname):
        self.driver.find_element(By.ID,(self.txtFirstName_id)).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element(By.ID,(self.txtLastName_id)).send_keys(lname)

    def SetGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID,(self.rdMaleGender_id)).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,(self.rdFemaleGender_id)).click()
        else:
            self.driver.find_element(By.ID,(self.rdMaleGender_id)).click()

    def SetDOB(self, dob):
        self.driver.find_element(By.NAME,(self.txtDob_name)).send_keys(dob)

    def SetCompany(self, company):
        self.driver.find_element(By.ID,(self.txtCompany_id)).send_keys(company)

    def SetNewsLetter(self,):
        self.driver.find_element(By.XPATH,(self.txtNewsLetter_xpath)).send_keys(Keys.TAB)
        # self.a=ActionChains(self.driver)
        # self.NL=self.driver.find_element(By.XPATH,(self.SetCustomersRoles))
        # self.a.move_to_element(self.NL).click().perform()


        # drp=Select(self.driver.find_element(By.ID,"SelectedNewsletterSubscriptionStoreIds"))
        # if Newsletter=="Your store name":
        #     self.listitem=self.driver.find_element(By.LINK_TEXT,(self.sltitemStoreNAme_link_text))
        # # elif Newsletter=="Test store 2":
        # #     self.listitem=self.driver.find_element(By.LINK_TEXT,(self.sltitemTestStore_link_text))
        # else:
        #     self.listitem=self.driver.find_element(By.LINK_TEXT,(self.sltitemTestStore_link_text))
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click()", self.listitem)

    def SetCustomersRoles(self, role):
        self.driver.find_element(By.XPATH,(self.txtCompanyroles_xpath)).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemRegistered_xpath))
        elif role == 'Administrators':
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemAdministrators_xpath))
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_taglist']//span[@title='delete']").click()
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemGuests_xpath))
        elif role == "Registered":
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemRegistered_xpath))
        elif role == "Vendors":
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemVendors_xpath))
        else:
            self.listitem1 = self.driver.find_element(By.XPATH,(self.lstitemGuests_xpath))
        time.sleep(3)
        self.driver.execute_script("arguments[0].click()",self.listitem1)

    def SetManagerOfvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH,(self.lstitemVendors_xpath)))
        drp.select_by_value(value)

    def SetAdminComment(self, comment):
        self.driver.find_element(By.ID,(self.txtAdminComment_id)).send_keys(comment)

    def ClickSave(self):
        self.driver.find_element(By.XPATH,(self.btnSave_xpath)).click()





