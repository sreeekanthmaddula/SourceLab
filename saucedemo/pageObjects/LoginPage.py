import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    # Login Page
    User_Name_Xpath = "//input[@id='user-name']"
    Password_Xpath = "//input[@id='password']"
    Login_Xpath = "//input[@id='login-button']"
    Homepage_Value="Swag Labs"
    locked_user_value="//button[@data-test='error-button']/parent::h3"

    def __init__(self,driver):
        self.driver=driver




    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.User_Name_Xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.Password_Xpath).send_keys(password)

    def clickLogin(self):
         self.driver.find_element(By.XPATH, self.Login_Xpath).click()

    def getText(self):
        return self.driver.find_element(By.XPATH,self.locked_user_value).text

    # def clickLogout(self):
    #
    #     self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()