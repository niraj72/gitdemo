from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
from Locators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.email = (By.NAME, HomePageLocators.email)
        self.name = (By.CSS_SELECTOR, HomePageLocators.name)
        self.check = (By.ID, HomePageLocators.check)
        self.gender = (By.ID, HomePageLocators.gender)
        self.submit = (By.XPATH, HomePageLocators.submit)
        self.successMessage = (By.CSS_SELECTOR, HomePageLocators.successMessage)
        self.shop = (By.CSS_SELECTOR, HomePageLocators.shop)


    def shopItems(self):
        self.driver.find_element(*self.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*self.name)

    def getEmail(self):
        return self.driver.find_element(*self.email)

    def getCheckBox(self):
        return self.driver.find_element(*self.check)

    def getGender(self):
        return self.driver.find_element(*self.gender)

    def submitForm(self):
        return self.driver.find_element(*self.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*self.successMessage)