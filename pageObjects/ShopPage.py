from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    phonesParent = (By.XPATH, "//div[@class='card h-100']")
    phoneModel = (By.XPATH, "div/h4/a")
    AddToCartButton = (By.XPATH, "div/button")
    checkOutButton = (By.XPATH, "//a[contains(@class, 'btn-primary')]")

    def getPhonesParent(self):
        """This returns a list of all the blocks which contains phones"""
        return self.driver.find_elements(*ShopPage.phonesParent)

    def getPhoneModel(self, phoneParentblock):
        """one element can be selected from the returned list from getPhonesParent and find title from it"""
        return phoneParentblock.find_element(*ShopPage.phoneModel)

    def getAddToCartButton(self, phoneParentblock):
        """one element can be selected from the returned list from getPhonesParent and find AddToCartButton from it"""
        return phoneParentblock.find_element(*ShopPage.AddToCartButton)

    def getCheckOutButton(self):
        """This returns the checkout button in Shop Page"""
        self.driver.find_element(*ShopPage.checkOutButton).click()
        objCheckOutPage = CheckOutPage(self.driver)
        return objCheckOutPage

