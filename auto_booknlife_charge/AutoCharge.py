from optparse import Option
from posixpath import split
from selenium import webdriver
import time as t
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


print(datetime.now())

pin_num = "0000-1111-2222-3333-4444"
list_pin_num = pin_num.split('-')
#=====================초기변수 선언=========================
ID = "ID"
PW = "PW"
driver_path ='C:/python/Discord_Bot/auto_cultureland_charge/chromedriver.exe'
# chrome_options = webdriver.ChromeOptions()


while True:
    # driver = webdriver.Chrome(driver_path, options=chrome_options)
    options = Options()
    options.add_extension("C:/python/Discord_Bot/auto_booknlife_charge/mpbjkejclgfgadiemmefgebjfooflfhl.crx")
    # options.add_argument("--incognito")
    driver = webdriver.Chrome(driver_path, options = options)
    #=======================================================
    
    
    
    #==============탭 열기=================
    driver.get("https://www.booknlife.com/hp/main.do")
    #==============================================

    driver.find_element_by_id('userID').send_keys(ID)

    driver.find_element_by_id('userPWD').send_keys(PW)

    driver.find_element_by_id('btn_login').click()
    accept_message = driver.switch_to_alert()
    accept_message.accept()
    print("reCAPTCHA 해제 시작...")
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[6]/div[4]/iframe")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button-holder.help-button-holder"))).click()
    
    while True:
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-verify-button")))
            t.sleep(0.5)
            continue
        except:
            break
        
    driver.switch_to.default_content()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btn_login"))).click()
        print("reCAPTCHA 해제 성공!")
    except:
        print("reCAPTCHA 해제 실패 restarting...")
        driver.quit()
        del driver
        del options
        continue
    print("충전 시도중...")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="contArea"]/div/div[1]/div[2]/div/div/dl/dt/a[2]')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="aMain_CashChargeConfirm"]'))).click()
    driver.switch_to.default_content()
    
    for i in range(0,len(list_pin_num) - 1):
        print(i)
        print(list_pin_num[i])
        driver.find_element_by_xpath(f'//*[@id="frmCashCharge"]/div/div[2]/table/tbody/tr[1]/td[2]/input[{i + 1}]').send_keys(list_pin_num[i])
    driver.find_element_by_xpath(f'//*[@id="frmCashCharge"]/div/div[2]/table/tbody/tr[1]/td[3]/input').send_keys(list_pin_num[-1])
    driver.find_element_by_xpath('//*[@id="frmCashCharge"]/div/div[2]/table/tbody/tr[1]/td[4]/button').click()
    
    break

    