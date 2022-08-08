import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('basic info','baseurl')
        return url
    @staticmethod
    def getUsermail():
        username=config.get('basic info','useremail')
        return username
    @staticmethod
    def getPassword():
        password=config.get('basic info','password')
        return password