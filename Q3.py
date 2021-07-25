# 1. Openning Walla via Chrome


from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:/Lab/chromedriver/chromedriver.exe")
browser.get("https://www.walla.co.il")
browser.close()

# 2. Openning Ynet via Firefox

from selenium import webdriver
browser = webdriver.Firefox(executable_path="C:/Lab/firefoxdriver/geckodriver.exe")
browser.get("https://ynet.co.il")
browser.close()

# 3. # Openning one via IE
from selenium import webdriver
browser = webdriver.ie(executable_path="C:\Lab\IEdriver\IEDriverServer.exe")
browser.get("https://one.co.il")
browser.close()


## The browser opening procedure is equal