from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObjects.CheckoutPage import CheckOutPage
from Locators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.shop = driver.find_element(By.CSS_SELECTOR, HomePageLocators.shop)
        self.name = driver.find_element(By.CSS_SELECTOR, HomePageLocators.name)
        self.email = driver.find_element(By.NAME, HomePageLocators.email)
        self.check = driver.find_element(By.ID, HomePageLocators.check)
        self.gender = driver.find_element(By.ID, HomePageLocators.gender)
        self.submit = driver.find_element(By.XPATH, HomePageLocators.submit)
        self.successMessage = driver.find_element(By.CSS_SELECTOR, HomePageLocators.successMessage)


    def shopItems(self):
        self.shop.click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getCheckBox(self):
        return self.check

    def getGender(self):
        return self.gender

    def submitForm(self):
        return self.submit

    def getSuccessMessage(self):
        return self.successMessage




