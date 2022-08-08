import pytest
import random
import string
import time
from selenium.webdriver.common.by import By
from pageobjects.LoginPage import LoginPage
from pageobjects.addCustomerPage import AddCustomer
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen


class Test_003_AddCustomer:
    baseurl = Readconfig.getApplicationURL()
    username = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info('*******Test_003_AddCustomer*****')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()

        self.logger.info('****Succesfully Login*****')
        self.logger.info('****Starting Add_Customers test****')

        self.ac = AddCustomer(self.driver)
        self.ac.ClickOnCustomerMenu()
        self.ac.ClickOnCustomerMenuItem()
        # self.ac.ClickOnAddCustomer()

        self.logger.info('*******provide customers info******')

        self.email=random_generator()+'@gmail.com'
        self.ac.SetEmail(self.email)
        self.ac.SetPassword('Test123')
        self.ac.SetFirstName('Pavan')
        self.ac.SetLastName('Kumar')
        self.ac.SetGender('Male')
        self.ac.SetDOB("8/5/1997")
        self.ac.SetCompany("ebm")
        # self.ac.SetNewsLetter("Your store name")
        self.ac.SetCustomersRoles("Guests")
        self.ac.SetManagerOfvendor("Vendor 1")
        self.ac.SetAdminComment("Thanks for registartion")
        self.ac.ClickSave()

        self.logger.info('********save  customer info*****')

        self.logger.info('*****Add customer validation started*****')

        self.msg = self.driver.find_element((By.XPATH, "//div[@class='alert alert-success alert-dismissable']")).text
        print(self.msg)

        if " customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*****Add customer test passed****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Add_customer_page.png")
            assert False == False
            self.logger.info("****Add customer test fialed*****")

        self.driver.close()
        self.logger.info("*****Ending Hoge page title*****")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# pytest -v -s --html=Report\report.html testCases/test_addCustomer.py --browser chrome