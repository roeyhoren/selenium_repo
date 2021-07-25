# 1. Openning Walla via Chrome
import time

from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:/Lab/chromedriver/chromedriver.exe")
browser.get("https://www.walla.co.il")
walla_title = browser.title
print(walla_title)
browser.refresh()
browser_chrome = browser.name
if walla_title!=browser_chrome:
    print("the names are not equal")
else:
    print(" names are equal")
time.sleep(1)
browser.close()

# 2. Openning Ynet via Firefox


from selenium import webdriver
browser = webdriver.Firefox(executable_path="C:/Lab/firefoxdriver/geckodriver")
browser.get("https://ynet.co.il")
ynet_title = browser.title
print(ynet_title)
browser.refresh()
browser_firefox = browser.name
if ynet_title!=browser_firefox:
    print("the names are not equal")
else:
    print(" names are equal")
time.sleep(1)
browser.close()


