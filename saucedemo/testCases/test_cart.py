import logging
import time
import pytest

from saucedemo.pageObjects.CartDetails import CartDetails
from saucedemo.pageObjects.LoginPage import LoginPage
from saucedemo.pageObjects.ProductPage import ProductPage
from saucedemo.utilities.readProperties import ReadConfig
from saucedemo.utilities.customLogger import LogGen
from saucedemo.pageObjects.ProductDetails import ProductDetails


class Test_Cart():
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.cart
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
        self.cd=CartDetails(self.driver)
        self.cd.addtoCart()
        cart_added_value=self.cd.Cart_Value
        time.sleep(5)
        if cart_added_value == "Remove":
            self.logger.info("****Cart added test passed ****")
            assert True
        else:
            self.logger.error("****Cart added  test failed ****")
            assert False

