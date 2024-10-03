import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductPage:
    # Product Page
    Product_details_Xpath = "//div[contains(text(), 'Backpack')]"
    Product_Value="Sauce Labs Backpack"


    def __init__(self,driver):
        self.driver=driver


    def searchProduct(self):
        self.driver.find_element(By.XPATH, self.Product_details_Xpath).click()

