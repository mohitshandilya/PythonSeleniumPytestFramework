from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    locationField = (By.XPATH, "//input[contains(@class, 'filter-input' )]")
    countrySuggestionsList = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    termsAndAgreementsCheckBox = (By.CSS_SELECTOR, "div[class*='checkbox']")
    purchaseButton = (By.XPATH, "//input[contains(@class,'btn-success')]")
    successText = (By.XPATH, "//div[contains(@class,'alert-success')]")

    def getLocationField(self):
        return self.driver.find_element(*PurchasePage.locationField)

    def getCountrySuggestionsList(self):
        return self.driver.find_elements(*PurchasePage.countrySuggestionsList)

    def getTermsAndAgreementsCheckBox(self):
        return self.driver.find_element(*PurchasePage.termsAndAgreementsCheckBox)

    def getpurchaseButton(self):
        return self.driver.find_element(*PurchasePage.purchaseButton)

    def getSuccessText(self):
        return self.driver.find_element(*PurchasePage.successText)