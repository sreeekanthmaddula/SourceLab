import logging
import time
import pytest
from saucedemo.pageObjects.LoginPage import LoginPage
from saucedemo.pageObjects.ProductPage import ProductPage
from saucedemo.utilities.readProperties import ReadConfig
from saucedemo.utilities.customLogger import LogGen
from saucedemo.pageObjects.ProductDetails import ProductDetails


class Test_ProductDetails():
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.productdetails
    # @pytest.mark.regression
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
        self.pd = ProductDetails(self.driver)
        prodcut_value = self.pd.Product_Value
        if prodcut_value == "Sauce Labs Backpack":
            self.logger.info("****Prodcuts details test passed ****")
            assert True
        else:
            self.logger.error("****Products details test failed ****")
            assert False
