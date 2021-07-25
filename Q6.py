from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path="C:/Lab/chromedriver/chromedriver.exe")
browser.get("https://translate.google.co.il")
browser.find_element_by_id("yDmH0d").send_keys("Nothing to translate")
time.sleep(1)
browser.close()

browser = webdriver.firefox(executable_path="C:/Lab/firefoxdriver/geckodriver.exe")
browser.get("https://translate.google.co.il")
browser.find_element_by_id("yDmH0d").send_keys("Nothing to translate")
time.sleep(1)
browser.close()

browser = webdriver.firefox(executable_path="C:\Lab\IEdriver\IEDriverServer.exe")
browser.get("https://translate.google.co.il")
browser.find_element_by_id("yDmH0d").send_keys("Nothing to translate")
time.sleep(1)
browser.close()

