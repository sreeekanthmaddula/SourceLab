import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class CartDetails:
    # Product Page
    Cart_details_Xpath = "//button[contains(text(), 'Add to cart')]"
    Cart_Value="Remove"


    def __init__(self,driver):
        self.driver=driver


    def addtoCart(self):
        self.driver.find_element(By.XPATH, self.Cart_details_Xpath).click()

    def validateCart(self):
        return self.driver.find_element(By.XPATH,self.Cart_Value).text