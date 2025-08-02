import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login import Login
from pages.hepigopin import Hepigopin
from pages.homepage import Homepage
import allure
import pytest
from data.login import Data_login
# data = [Data_login.user1,Data_login.user2]
#data = [(driver1)]


@allure.title("test positive login")
@allure.description("this test case only positive login, not comprehensive case")
@allure.tag("Regression")
@allure.severity(allure.severity_level.CRITICAL)
#@pytest.mark.parametrize("NomorHp,Password",data)

def test_positive_login(driver1):
    login = Login(driver1)
    hepigopin = Hepigopin(driver1)
    homepage = Homepage(driver1)
    
    login.skipintro()
    login.input_username("081288219696")
    login.input_password("Carlo19#")
    login.click_buttonlogin()

    hepigopin.input_PIN()
    homepage.click_closetooltip()
    homepage.click_closepopup()

    with allure.step("verify usernamelogin"):
        assert homepage.verify_name() == 'Halo, Carl Naiwan'

def test_positive_login2(driver2):
    login = Login(driver2)
    hepigopin = Hepigopin(driver2)
    homepage = Homepage(driver2)
    
    login.skipintro()
    login.input_username("081275551979")
    login.input_password("Carlo19#")
    login.click_buttonlogin()

    hepigopin.input_PIN()

    homepage.click_closetooltip()
    homepage.click_closepopup()

    with allure.step("verify usernamelogin"):
        assert homepage.verify_name() == 'Halo, Fitria Rafles'