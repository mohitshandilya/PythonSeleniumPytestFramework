from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')

    def NavigateToShopPage(self):
        self.driver.find_element(*HomePage.shop).click()
        objShopPage = ShopPage(self.driver)
        return objShopPage

