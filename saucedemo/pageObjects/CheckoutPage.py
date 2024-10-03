import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkoutdetails:
    # Product Page
    Checout_details_Xpath = "//div[@id='shopping_cart_container']/a/span"
    checkout_confirm_Xpath="//button[text()='Checkout']"
    checkout_value="Checkout: Your Information"


    def __init__(self,driver):
        self.driver=driver


    def checkoutDetails(self):
        self.driver.find_element(By.XPATH, self.Checout_details_Xpath).click()

    def validatecheckoutdetails(self):
        return self.driver.find_element(By.XPATH,self.checkout_value).text