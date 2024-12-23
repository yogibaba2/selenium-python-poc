from selenium import webdriver
from selenium_stealth import stealth

# create ChromeOptions object
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Set up WebDriver
driver = webdriver.Chrome(options=options)

# Open a webpage
driver.get("https://opensea.io/")
print(driver.title)

driver.quit()
