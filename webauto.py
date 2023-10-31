from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username= driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password= driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login=driver.find_element(By.ID, "login-button").click()
time.sleep(5)

Addbutton=driver.find_element(By.CLASS_NAME, "btn_primary")
for button in Addbutton :
    
    button.click()
    time.sleep(5)
    