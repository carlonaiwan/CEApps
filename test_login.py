import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_positive_login(driver):
    # Skip 'Lewati' jika ada
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Lewati']").click()
    except NoSuchElementException:
        print("Lewati tidak muncul, lanjut.")

    # Masukkan username dan password
    driver.find_element(AppiumBy.XPATH,
        "(//android.widget.EditText[@content-desc='inputFormik_id_q0sigmpf'])[1]"
    ).send_keys("081288219696")

    driver.find_element(AppiumBy.XPATH,
        "(//android.widget.EditText[@content-desc='inputFormik_id_q0sigmpf'])[2]"
    ).send_keys("Carlo19#")

    driver.find_element(AppiumBy.XPATH,
        "//android.widget.TextView[@text='MASUK']"
    ).click()

    # Masukkan PIN jika diminta
    try:
        sleep(10)
        driver.find_element(AppiumBy.XPATH,
            "//android.widget.TextView[@text='MASUK']/parent::*"
        ).click()

        for pin in ["1", "5", "9", "3", "5", "7"]:
            driver.find_element(AppiumBy.XPATH,
                f"//android.widget.TextView[@text='{pin}']/parent::*"
            ).click()
    except NoSuchElementException:
        print("PIN tidak diperlukan, lanjut.")

    
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
                "//android.widget.TextView[@text='NANTI SAJA']/parent::*"
            ))
        )
        element.click()
    except TimeoutException:
        print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")
