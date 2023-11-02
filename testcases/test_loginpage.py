import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from testcases.BaseTest import BaseTest
from POM_Login.LoginPage import Login
# from testcases.conftest import BaseTest


class Test_Login(BaseTest):


    def test_login1(self, driver):
        objlogin = Login(self, driver)
        objlogin.login("Admin","admin123")

    # def test_login_title(self):
    #     obj = Login()
    #     title = obj.get_title("OrangeHRM")
    #     assert title == "OrangeHRM"

    # def test_login(self, driver):
    #     self.loginobj = Login(self, driver)
    #   # title =self.loginobj.get_title("OrangeHRM")
    #    # assert title == "OrangeHRM"
    #     self.loginobj.login("Admin","admin123")