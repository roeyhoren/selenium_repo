from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path="C:/Lab/chromedriver/chromedriver.exe")
browser.get("https://translate.google.co.il")
browser.find_element_by_id("yDmH0d").send_keys("mark knopfler brothers in arms")
time.sleep(1)




