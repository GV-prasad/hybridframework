import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from pageobjects.searchCustomerPage import searchCustomer
from pageobjects.addCustomerPage import AddCustomer
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen
import time
