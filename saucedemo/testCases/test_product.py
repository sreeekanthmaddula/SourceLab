import logging
import time
import pytest
from saucedemo.pageObjects.LoginPage import LoginPage
from saucedemo.pageObjects.ProductPage import ProductPage
from saucedemo.utilities.readProperties import ReadConfig
from saucedemo.utilities.customLogger import LogGen


class Test_Product():
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.product
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        ecomm_title = self.lp.Homepage_Value
        if ecomm_title == "Swag Labs":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            assert False
        self.pp.searchProduct()
        time.sleep(5)
        prodcut_value = self.pp.Product_Value
        if prodcut_value == "Sauce Labs Backpack":
            self.logger.info("****Prodcuts search test passed ****")
            assert True
        else:
            self.logger.error("****Products search test failed ****")
            assert False
