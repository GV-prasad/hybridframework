import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen


class Test_001_Login:
    baseurl=Readconfig.getApplicationURL()
    username=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_homepagetitle(self,setup):

        self.logger.info('******Test_001_Login******')
        self.logger.info('******verifying_homepage_title******')
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            self.logger.info('****home_page _title is passed************')
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "homepagetitle.png")
            self.logger.error("****home_page_title is failed******")
            self.driver.close()
            assert False

    def test_Login_page_title(self,setup):

        self.logger.info('*****verify login page*****')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info('******login page is passed****')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "LoginPageTitle.png")
            self.logger.error('*****login page is failed****')
            self.driver.close()
            assert False







