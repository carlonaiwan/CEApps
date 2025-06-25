import pytest
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = "R9RX2004DRA"
    options.app_package = "com.hso.motorku"
    options.app_activity = "com.hso.motorku.MainActivity"
    options.auto_grant_permissions = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(30)
    yield driver
    #driver.quit()
