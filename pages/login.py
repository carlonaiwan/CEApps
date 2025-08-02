import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.login import Locator
import allure


class Login:
    def __init__(self,driver):
        self.driver = driver
    
    def skipintro(self):
        with allure.step("Skip Intro"):
            try:
                self.driver.find_element(AppiumBy.XPATH,Locator.btn_Lewati).click()
            except NoSuchElementException:
                print("Lewati tidak muncul, lanjut.")
    
    def input_username(self, NomorHp):
        with allure.step("input_username"):
            self.driver.find_element(AppiumBy.XPATH,Locator.input_NoHp).send_keys(NomorHp)
    
    def input_password(self, Password):
        with allure.step("input_password"):
            self.driver.find_element(AppiumBy.XPATH,Locator.input_Password).send_keys(Password)
    
    def click_buttonlogin(self):
        with allure.step("click_buttonlogin"):
            self.driver.find_element(AppiumBy.XPATH,Locator.btn_Masuk).click()

    

    
