from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


options1 = UiAutomator2Options()
options1.platform_name = "Android"
options1.udid = "R9RX2004DRA"
options1.app_package = "com.hso.motorku"
options1.app_activity = "com.hso.motorku.MainActivity"
#for grant access popup
options1.auto_grant_permissions = True
#1 port = 1 device, but on range 4700

driver = webdriver.Remote("http://127.0.0.1:4723",options=options1)

#waiting fot element
driver.implicitly_wait(30)

try:
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Lewati']").click()
except NoSuchElementException:
    print("Tombol 'Lewati' tidak ditemukan, lanjut ke langkah berikutnya.")

driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@content-desc='inputFormik_id_q0sigmpf'])[1]").send_keys("081288219696")
driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@content-desc='inputFormik_id_q0sigmpf'])[2]").send_keys("Carlo19#")
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='MASUK']").click()

try:
    sleep(5)
    #cause apps not can't handle speed automation,
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='MASUK']/parent::*").click()
    #driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='MASUK']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='1']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='5']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='9']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='3']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='5']/parent::*").click()
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='7']/parent::*").click()

except NoSuchElementException:
    print("Tombol 'Masuk PIN' tidak ditemukan, dan tidak diperlukan input pin")



try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((
            AppiumBy.XPATH, 
            "//android.widget.TextView[@text='Tutup']"
        ))
    )
    element.click()
except TimeoutException:
    print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")



try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((
            AppiumBy.XPATH, 
            #call xpath on parent if child not clickable
            #/parent::* & /child::*
           "//android.widget.TextView[@text='NANTI SAJA']/parent::*"
           
        ))
    )
    element.click()
except TimeoutException:
    print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")




