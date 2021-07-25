from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path="C:/Lab/chromedriver/chromedriver.exe")
browser.get("https://facebook.com")
browser.find_element_by_id("email").send_keys("roeyhoren@gmail.com")
time.sleep(1)
browser.find_element_by_id("pass").send_keys("123123")
time.sleep(1)
browser.find_element_by_id("u_0_d_Wm").send_keys(Keys.ENTER)


