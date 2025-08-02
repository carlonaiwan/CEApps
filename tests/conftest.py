import pytest
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import allure


@pytest.fixture(scope="function")
def driver1():
    with allure.step("Setup Device and Open Apps"):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.udid = "192.168.1.7:5556"
        options.app_package = "com.hso.motorku"
        options.app_activity = "com.hso.motorku.MainActivity"
        options.auto_grant_permissions = True

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        driver.implicitly_wait(30)
    yield driver
    with allure.step("Close Apps"):
        driver.quit()

@pytest.fixture(scope="function")
def driver2():
    with allure.step("Setup Device and Open Apps"):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.udid = "192.168.1.9:5555"
        options.app_package = "com.hso.motorku"
        options.app_activity = "com.hso.motorku.MainActivity"
        options.auto_grant_permissions = True

        driver = webdriver.Remote("http://127.0.0.1:4724", options=options)
        driver.implicitly_wait(30)
    yield driver
    with allure.step("Close Apps"):
        driver.quit()        
