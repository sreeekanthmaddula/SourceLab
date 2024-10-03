import logging
import time
import pytest
from saucedemo.pageObjects.LoginPage import LoginPage
from saucedemo.utilities.readProperties import ReadConfig
from saucedemo.utilities.customLogger import LogGen


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    lockedout_username=ReadConfig.getLocked_Username()
    problem_username=ReadConfig.getProblem_Username()
    performance_username=ReadConfig.getPerforamce_Username()
    invalid_username=ReadConfig.getInvalid_Username()
    logger = LogGen.loggen()

    @pytest.mark.login
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test for automation ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        time.sleep(5)
        ecomm_title = self.driver.title
        if ecomm_title == "Swag Labs":
            self.logger.info("**** Home page title test passed ****")
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            assert False

    @pytest.mark.login
    # @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
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

    @pytest.mark.login
    def test_locked_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.lockedout_username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        locked_user_title = self.lp.getText()
        print(locked_user_title)
        if locked_user_title == "Epic sadface: Sorry, this user has been locked out.":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            assert False

    @pytest.mark.login
    def test_problem_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.problem_username)
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


    @pytest.mark.login
    def test_performance_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.performance_username)
        self.lp.setPassword(self.passworsd)
        self.lp.clickLogin()
        time.sleep(10)
        ecomm_title = self.lp.Homepage_Value
        if ecomm_title == "Swag Labs":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            assert False

    @pytest.mark.login
    def test_invalid_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.invalid_username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        invalid_title = self.lp.getText()
        if invalid_title == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            assert False

    @pytest.mark.login
    def test_missed_cred_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        time.sleep(10)
        invalid_title = self.lp.getText()
        if invalid_title == "Epic sadface: Username is required":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            assert False

