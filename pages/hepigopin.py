
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.hepigopin import Locator
import allure

class Hepigopin:
    def __init__(self,driver):
        self.driver = driver

    def input_PIN(self):
        with allure.step("input_PIN"):    
            # Masukkan PIN jika diminta
            try:
                sleep(10)
                self.driver.find_element(AppiumBy.XPATH,Locator.btn_masukpin).click()

                for pin in ["1", "5", "9", "3", "5", "7"]:
                    self.driver.find_element(AppiumBy.XPATH,f"//android.widget.TextView[@text='{pin}']/parent::*").click()
            except NoSuchElementException:
                print("PIN tidak diperlukan, lanjut.")