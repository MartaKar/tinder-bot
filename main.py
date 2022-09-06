
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

ser = Service("/Users/marta/Downloads/chromedriver")

driver = webdriver.Chrome(service=ser)

driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(4)

log_in = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
time.sleep(2)
facebook_log_in = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook_log_in.click()
time.sleep(4)
parent = driver.current_window_handle
windows = driver.window_handles
driver.switch_to.window(windows[-1])
cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
cookies.click()
email = driver.find_element(By.ID, "email")
email.send_keys("kamarta35@gmail.com")
password = driver.find_element(By.ID, "pass")
password.send_keys("4pStf2Tt6SEp35h")
login = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
login.click()
driver.switch_to.window(parent)
driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button').click()
time.sleep(6)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(2)
swipe = True
while swipe is True:
    body = driver.find_element(By.XPATH, '/html/body')
    body.send_keys(Keys.LEFT)
    time.sleep(3)
    # try:
    #     driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button').click()
    #     time.sleep(3)
    # except NoSuchElementException:
    #     pass






