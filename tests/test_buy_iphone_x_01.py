import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.PurchasePage import PurchasePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestClass(BaseClass):

    def test_buy_iphone_x_01(self):
        log = self.getLogger()
        objHomePage = HomePage(self.driver)

        objShopPage = objHomePage.NavigateToShopPage()  # Navigate to shop page and Create ShopPage Object

        phonesParent = objShopPage.getPhonesParent()

        for phone in phonesParent:
            phoneModel = objShopPage.getPhoneModel(phone).text
            log.info("Phone Element is : {}".format(phone))
            log.info("Phone Model is : {}".format(phoneModel))
            if phoneModel == "iphone X":
                objShopPage.getAddToCartButton(phone).click()  # Add Iphone X to cart
                break
            else:
                log.error("Error Occurred : Model Iphone X do not exists")
                assert 0
        # click the checkout button
        objCheckOutPage = objShopPage.getCheckOutButton() # CLick CheckOut Button in Shop Page and
                                                          # Navigate to CheckOut Page and create CheckOutPage Object

        self.ExplicitWaitForAllPageElements(3) #Explicitly wait for 10 seconds for all Page elements to Appear
        objPurchasePage = objCheckOutPage.getCheckOutButton() # CLick CheckOut Button in CheckOut Page and
                                                              # Navigate to Purchase Page and create PurchasePage Object

        self.ExplicitWaitForAllPageElements(3) #Explicitly wait for 10 seconds for all Page elements to Appear
        objPurchasePage.getLocationField().send_keys("Ind")


        self.ExplicitWaitUntilElementPresence(objPurchasePage.countrySuggestionsList, 7)

        suggestedCountriesList = objPurchasePage.getCountrySuggestionsList()

        for location in suggestedCountriesList:
            if location.text == "India":
                location.click()
                break
            else:
                log.error("Error Occurred. Location India not found in the List")
                assert 0

        objPurchasePage.getTermsAndAgreementsCheckBox().click()
        # self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
        # //input[contains(@class,"btn-success")]

        objPurchasePage.getpurchaseButton().click()

        sucessText = objPurchasePage.getSuccessText().text
        validationText = "Success! Thank you!"

        try:
            assert validationText in sucessText
            log.info("Test Case Passed.")
            print("test Passed")
        except Exception as e:
            log.error("Error Occurred - Test Failed as the text do not match")
