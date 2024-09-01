from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PATH = "C:/Users/91630/OneDrive - Indian Institute of Technology Guwahati/Desktop/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://techwithtim.net")
print(driver.title)
time.sleep(10)

driver.quit()
