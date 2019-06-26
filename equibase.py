import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER_PATH=r"./chrome_driver/chromedriver.exe"
options = Options()
options.headless = False
username = os.getenv("USERNAME")
userProfile = "C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}".format(userProfile))
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
options.add_argument("user-agent=firefox")

driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=options)
driver.get("http://www.equibase.com/stats/")
element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "find"))
)
element.send_keys("Right the Wrong")
element.send_keys(Keys.ENTER)
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Right the Wrong"))
).click()


