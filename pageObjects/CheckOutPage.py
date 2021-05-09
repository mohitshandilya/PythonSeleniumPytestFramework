from selenium.webdriver.common.by import By

from pageObjects.PurchasePage import PurchasePage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    checkOutButton = (By.XPATH, "//button[contains(@class,'btn-success')]")

    def getCheckOutButton(self):
        """ Navigates to PurchasePage and returns the PurchasePage Object """
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        objPurchasePage = PurchasePage(self.driver)
        return objPurchasePage