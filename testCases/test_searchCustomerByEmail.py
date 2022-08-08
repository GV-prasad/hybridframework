import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from pageobjects.searchCustomerPage import searchCustomer
from pageobjects.addCustomerPage import AddCustomer
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen
import time

class Test_searchCustomerByEmail_004:
    baseurl=Readconfig.getApplicationURL()
    username=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_searchByemail(self,setup):
        self.logger.info("*** Test_searchCustomerByEmail_004***")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(5)

        self.logger.info("***Login****")
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        self.logger.info("***Succesfully login***")
        time.sleep(5)

        self.logger.info("***Starting search customer by email***")
        self.ac = AddCustomer(self.driver)
        self.ac.ClickOnCustomerMenu()
        self.ac.ClickOnCustomerMenuItem()
        # self.ac.ClickOnAddCustomer()
        time.sleep(10)

        self.logger.info('***search customer by email id**')
        searchCust=searchCustomer(self.driver)
        searchCust.setEmail("james_pan@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(5)

        status=searchCust.searchCustomerByemail("james_pan@nopCommerce.com")
        assert True==status
        self.logger.info("****TC_search customer by email is finished****")
        self.driver.close()
