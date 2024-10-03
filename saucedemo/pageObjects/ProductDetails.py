import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductDetails:
    # Product Page
    Product_search_Xpath = "//div[contains(text(), 'Backpack')]"
    Product_Value="Sauce Labs Backpack"


    def __init__(self,driver):
        self.driver=driver


    def productDetails(self):
        return self.driver.find_element(By.XPATH,self.Product_search_Xpath).text


