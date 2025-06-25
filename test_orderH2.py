import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_positive_orderH2(driver):
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
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, 
                "//android.widget.TextView[@text='Tutup']"
            ))
        )
        element.click()
    except TimeoutException:
        print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")


    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH, 
                "//android.widget.TextView[@text='NANTI SAJA']/parent::*"
            ))
        )
        element.click()
    except TimeoutException:
        print("Timeout: Elemen tidak ditemukan dalam waktu 20 detik atau element tidak ditemukan.")

    sleep(5)
    driver.swipe(start_x=168, start_y=1544, end_x=168, end_y=400, duration=500)
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='BOOKING SERVIS']").click()
    except NoSuchElementException:
            print("Element 'Booking Servis' tidak muncul")

    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Pilih Lokasi Ahass']").click()
    except NoSuchElementException:
            print("element 'Pilih Lokasi Ahass' tidak muncul")

    sleep(5)
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Cari Lokasi Ahass']").click()
        driver.find_element(AppiumBy.XPATH,
            "(//android.widget.EditText[@text='Cari Lokasi Ahass'])[1]").send_keys("MANDIRI MOTOR")
        sleep(3)
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='MANDIRI MOTOR']").click()
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PILIH']").click()
    except NoSuchElementException:
            print(".....")

    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Pilih Hari/Tanggal']").click()
    except NoSuchElementException:
            print("element pilih tanggal servis tidak muncul")

    
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Next month").click()
        driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='19']").click()
        driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='OK']").click()
        
    except NoSuchElementException:
            print("......")
    
    try:
        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='09:00']").click()
        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='LANJUT']").click()
        
    except NoSuchElementException:
            print("......")
    

    try:
          driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText").send_keys("191919")
          driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Jenis Servis']")
          driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='LANJUT']")
          driver.find_element(AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc='setSubmitButton_id_vzoqaqif''])[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
          driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='LANJUT']")

    except NoSuchElementException:
            print("....")

    #scroll down kebawah sbntr ini belum nemu titik koordinat device nya :""""

    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='LANJUT']")



