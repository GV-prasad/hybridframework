from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        serv_obj = Service("C://DRIVER//chromedriver_win32//chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    else:
        driver=webdriver.Ie()

    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'prasad'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("plugins",None)

