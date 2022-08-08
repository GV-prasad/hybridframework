from selenium.webdriver.common.by import By
from selenium import webdriver

class searchCustomer:

    txtemail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"

    table_xpath="//div[@id='customers-grid_wrapper']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,(self.txtemail_id)).clear()
        self.driver.find_element(By.ID,(self.txtemail_id)).send_keys(email)
    def setFirstName(self,fname):
        self.driver.find_element(By.ID,(self.txtFirstName_id)).clear()
        self.driver.find_element(By.ID,(self.txtFirstName_id)).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,(self.txtLastName_id)).clear()
        self.driver.find_element(By.ID,(self.txtLastName_id)).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,(self.btnSearch_id)).click()

    def getNoOfRows(self):
        leght=len(self.driver.find_element(By.XPATH,(self.tableRows_xpath)))
        return leght

    def getNoOfColumns(self):
        length=len(self.driver.find_element(By.XPATH,(self.tableColumns_xpath)))
        return length

    def searchCustomerByemail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,(self.table_xpath))
            Emailid=table.find_element(By.XPATH,("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]")).text
            if Emailid==email:
                falg=True
                break
        return flag

    def searchCustomerByName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,(self.table_xpath))
            Name=table.find_element(By.XPATH("//table[@id='customers-grid']/tbody/tr("+str(r)+")/td[3]")).text
            if Name==name:
                flag=True
                break
        return flag

