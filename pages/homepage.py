import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.homepage import Locator
import allure

class Homepage:
    def __init__(self,driver):
        self.driver = driver

    def click_closetooltip(self):
        with allure.step("click_closetooltip"):
            try:
                element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, Locator.btn_tutuptooltip)))
                element.click()
            except TimeoutException:
                print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")

    def click_closepopup(self):
        with allure.step("click_closepopup"):    
            try:
                element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, Locator.btn_nantisajapopup)))
                element.click()
            except TimeoutException:
                print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")

    def verify_name(self):
        with allure.step("verify_name"):
            try:
                element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, Locator.obj_nameaccount)))
                name = element.text
            except TimeoutException:
                print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")
            return name
    
    def click_OrderH2card(self):
        with allure.step("click_OrderH2card"):
            try:
                self.driver.find_element(AppiumBy.XPATH,Locator.btn_orderH2card).click()
            except NoSuchElementException:
                print("Element 'Booking Servis' tidak muncul")


    