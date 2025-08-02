import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.login import Locator
from locators.orderH2 import Locator

class OrderH2_CardSection :
    def __init__(self,driver):
        self.driver = driver

    def click_PilihLokasiAHASS(self):
        try:
            self.driver.find_element(AppiumBy.XPATH,Locator.field_PilihLokasiAhass).click()
        except NoSuchElementException:
            print("element 'Pilih Lokasi Ahass' tidak muncul")
    
    